from django.db.models import Avg
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

from startapp.models import WaterData, PipelineRun, Country


def cleanData(filter_kwargs):
    if not isinstance(filter_kwargs, dict) or filter_kwargs == {}:
        queryset = WaterData.objects.all()
    else :
        queryset = WaterData.objects.filter(**filter_kwargs)

    yearly_data = queryset.values('phenomenonTimeReferenceYear').annotate(
                resultMeanValue=Avg('resultMeanValue')
            ).order_by('phenomenonTimeReferenceYear')
        
    df = pd.DataFrame(yearly_data)

    Q1 = df["resultMeanValue"].quantile(0.25)
    Q3 = df["resultMeanValue"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df_filtered = df[(df["resultMeanValue"] >= lower_bound) & (df["resultMeanValue"] <= upper_bound)]

    df_filtered['phenomenonTimeReferenceYear'] = pd.to_datetime(df_filtered['phenomenonTimeReferenceYear'], format='%Y')
    df_filtered['phenomenonTimeReferenceYear'] = df_filtered['phenomenonTimeReferenceYear'].dt.year

    X = np.array(df_filtered["phenomenonTimeReferenceYear"]).reshape(-1, 1)
    y = np.array(df_filtered["resultMeanValue"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    return X, y, X_train, X_test, y_train, y_test


@shared_task(bind=True)
def arimaForecasting(self, model, filter_kwargs, pipelineRunID):
    parameters = model['parameters']
    pipeline_run = PipelineRun.objects.get(id=pipelineRunID)

    try:
        pipeline_run.mark_started()

        X, y, X_train, X_test, y_train, y_test = cleanData(filter_kwargs)

        model_fitted = ARIMA(y_train, order=(int(parameters['p']['value']), int(parameters['d']['value']), int(parameters['q']['value']))).fit()

        years_to_predict = np.array([int(max(X)) + x for x in range(1, 6)]).reshape(-1, 1)

        y_forecasts = model_fitted.get_forecast(steps=len(years_to_predict)).predicted_mean
        y_pred = model_fitted.get_forecast(steps=len(X_test)).predicted_mean

        country_instance = Country.objects.filter(isoalpha2 = filter_kwargs['countryCode']).values_list("country", flat=True).first()

        results = {
            'country' : country_instance,
            'observedProperty' : filter_kwargs['observedPropertyDeterminandLabel'],
            'model': model['name'],
            'parameters': parameters,
            'series': [
                {
                    'name': 'Données historiques',
                    'type': 'line',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(X.flatten().tolist(), y.tolist())
                    ]
                },
                {
                    'name': 'Prédictions futures',
                    'type': 'line',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(years_to_predict.flatten().tolist(), y_forecasts.tolist())
                    ]
                }
            ],
            'metrics': {
                        'mean_absolute_error': float(mean_absolute_error(y_test, y_pred)),
                        'mean_squared_error': float(mean_squared_error(y_test, y_pred)),
                        'root_mean_squared_error': root_mean_squared_error(y_test, y_pred)
                    }
            }

        pipeline_run.results  = results
        pipeline_run.save()
        pipeline_run.mark_completed(success=True)

        return results

    except Exception as e:
        pipeline_run.mark_completed(success=False)
        raise e

@shared_task(bind=True)
def randomForestRegression(self, model, filter_kwargs, pipelineRunID):
    parameters = model['parameters']

    pipeline_run = PipelineRun.objects.get(id=pipelineRunID)

    try:
        pipeline_run.mark_started()

        X, y, X_train, X_test, y_train, y_test = cleanData(filter_kwargs)

        model_fitted = RandomForestRegressor(n_estimators=int(parameters['n_estimators']['value']), max_depth=int(parameters['max_depth']['value'])).fit(X_train, y_train)

        X_predicted = model_fitted.predict(X)

        years_to_predict = np.array([int(max(X)) + x for x in range(1, 6)]).reshape(-1, 1)

        y_forecasts = model_fitted.predict(years_to_predict)
        y_pred = model_fitted.predict(X_test)
        
        country_instance = Country.objects.filter(isoalpha2 = filter_kwargs['countryCode']).values_list("country", flat=True).first()

        results = {
            'country' : country_instance,
            'observedProperty' : filter_kwargs['observedPropertyDeterminandLabel'],
            'model': model['name'],
            'parameters': parameters,
            'series': [
                {
                    'name': 'Données observées',
                    'type': 'scatter',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(X.flatten().tolist(), y.tolist())
                    ]
                },
                {
                    'name': 'Droite de régression',
                    'type': 'line',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(X.flatten().tolist(), X_predicted.tolist())
                    ]
                },
                {
                    'name': 'Prédictions futures',
                    'type': 'scatter',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(years_to_predict.flatten().tolist(), y_forecasts.tolist())
                    ]
                }
            ],
            'metrics': {
                        'r_squared': float(model_fitted.score(X_train, y_train)),
                        'mean_absolute_error': float(mean_absolute_error(y_test, y_pred)),
                        'mean_squared_error': float(mean_squared_error(y_test, y_pred)),
                        'root_mean_squared_error': root_mean_squared_error(y_test, y_pred)
                    }
            }

        pipeline_run.results  = results
        pipeline_run.save()
        pipeline_run.mark_completed(success=True)

        return results

    except Exception as e:
        pipeline_run.mark_completed(success=False)
        raise e

@shared_task(bind=True)
def linearRegression(self, model, filter_kwargs, pipelineRunID):
    parameters = model['parameters']
    pipeline_run = PipelineRun.objects.get(id=pipelineRunID)

    try:
        pipeline_run.mark_started()

        X, y, X_train, X_test, y_train, y_test = cleanData(filter_kwargs)

        model_fitted = LinearRegression(fit_intercept=parameters['fit_intercept']['value']).fit(X_train, y_train)
        
        X_predicted = model_fitted.predict(X)

        years_to_predict = np.array([int(max(X)) + x for x in range(1, 6)]).reshape(-1, 1)

        y_forecasts = model_fitted.predict(years_to_predict)
        y_pred = model_fitted.predict(X_test)
        
        country_instance = Country.objects.filter(isoalpha2 = filter_kwargs['countryCode']).values_list("country", flat=True).first()

        results = {
            'country' : country_instance,
            'observedProperty' : filter_kwargs['observedPropertyDeterminandLabel'],
            'model': model['name'],
            'parameters': parameters,
            'series': [
                {
                    'name': 'Données observées',
                    'type': 'scatter',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(X.flatten().tolist(), y.tolist())
                    ]
                },
                {
                    'name': 'Droite de régression',
                    'type': 'line',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(X.flatten().tolist(), X_predicted.tolist())
                    ]
                },
                {
                    'name': 'Prédictions futures',
                    'type': 'scatter',
                    'data': [
                        {'x': year, 'y': value} for year, value in zip(years_to_predict.flatten().tolist(), y_forecasts.tolist())
                    ]
                }
            ],
            'metrics': {
                        'r_squared': float(model_fitted.score(X_train, y_train)),
                        'mean_absolute_error': float(mean_absolute_error(y_test, y_pred)),
                        'mean_squared_error': float(mean_squared_error(y_test, y_pred)),
                        'root_mean_squared_error': root_mean_squared_error(y_test, y_pred)
                    }
            }


        pipeline_run.results  = results
        pipeline_run.save()
        pipeline_run.mark_completed(success=True)

        return results

    except Exception as e:
        pipeline_run.mark_completed(success=False)
        raise e

