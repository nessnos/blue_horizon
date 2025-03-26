from django.urls import path

from . import api

urlpatterns = [
    path('data/', api.GetUniqueListData.as_view()),
    path('data/map/list-countries/', api.GetMapCountries.as_view()),
    path('data/map/general-info/', api.GeneralInfo.as_view()),
    path('data/pipelines/', api.Pipelines.as_view()),
    path('data/get-pipeline/', api.GetPipeline.as_view()),

    path('stats/dashboard/', api.GetDashBoardData.as_view()),

    path('ml/run/linear-regression', api.RunLinearRegression.as_view()),
    path('ml/run/rf-regression', api.RunRandomForestRegression.as_view()),
    path('ml/run/arima', api.RunARIMAForecasting.as_view()),

    path('chat/answer/', api.ChatCompletion.as_view()),
    path('chat/data/', api.CountryChat.as_view())
]
