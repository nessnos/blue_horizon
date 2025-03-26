from rest_framework.response import Response
from rest_framework.views import APIView

from startapp.models import PipelineRun
from startapp.tasks import linearRegression, randomForestRegression, arimaForecasting


class RunLinearRegression(APIView):
    def post(self, request):
        model = request.data.get('model')
        filter_kwargs = request.data.get('filter_kwargs', {})

        if model is None or filter_kwargs is None:
            return Response('Error')
        else:
            pipeline_run = PipelineRun.objects.create(
                model_name=model['name'],
                task_id='',
                status='PENDING'
            )

            task = linearRegression.delay(model, filter_kwargs, str(pipeline_run.id))

            pipeline_run.task_id = task.id
            pipeline_run.save()
        return Response({"task_id": task.id})


class RunRandomForestRegression(APIView):
    def post(self, request):
        model = request.data.get('model')
        filter_kwargs = request.data.get('filter_kwargs', {})

        if model is None or filter_kwargs is None:
            return Response('Error')
        else:
            pipeline_run = PipelineRun.objects.create(
                model_name=model['name'],
                task_id='',
                status='PENDING'
            )

            task = randomForestRegression.delay(model, filter_kwargs, str(pipeline_run.id))

            pipeline_run.task_id = task.id
            pipeline_run.save()
        return Response({"task_id": task.id})


class RunARIMAForecasting(APIView):
    def post(self, request):
        model = request.data.get('model')
        filter_kwargs = request.data.get('filter_kwargs', {})

        if model is None or filter_kwargs is None:
            return Response('Error')
        else:
            pipeline_run = PipelineRun.objects.create(
                model_name=model['name'],
                task_id='',
                status='PENDING'
            )

            task = arimaForecasting.delay(model, filter_kwargs, str(pipeline_run.id))

            pipeline_run.task_id = task.id
            pipeline_run.save()
        return Response({"task_id": task.id})
