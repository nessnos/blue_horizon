from rest_framework import serializers

from startapp.models import Country, PipelineRun, CountryStats


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='country')
    code = serializers.CharField(source='isoalpha2')

    class Meta:
        model = Country
        fields = ['code', 'name']


class MapCountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='country')
    code = serializers.CharField(source='iso_alpha2')
    clicked = serializers.BooleanField(default=False)

    class Meta:
        model = CountryStats
        fields = ['code', 'name', 'clicked']


class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipelineRun
        fields = ['id', 'task_id', 'status', 'model_name', 'started_at', 'completed_at', 'results']
