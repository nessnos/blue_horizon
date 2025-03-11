from rest_framework.response import Response
from rest_framework.views import APIView

from startapp.serializers import MapCountrySerializer,PipelineSerializer
from startapp.models import Filters, CountryStats, PipelineRun

class GetMapCountries(APIView):
     def get(self, request):
        return Response(MapCountrySerializer(CountryStats.objects.values('country', 'iso_alpha2').distinct(), many=True).data)

class GetUniqueListData(APIView):
    def post(self, request):
        include_all = request.query_params.get('include_all', 'false').lower() == 'true'
        include = request.data.get('include', [])
        filter_kwargs = request.data.get('filter_kwargs', {})
        results= {}

        countries = Filters.objects.values_list('country', 'iso_alpha2').order_by('country').distinct()
        countries = [{'name': name, 'code' : code} for name, code in countries]
        if include_all:
                countries = [{'name': 'Tout'}] + countries
        results['countries'] = countries
 
        if not isinstance(filter_kwargs, dict) or filter_kwargs == {'country': 'Tout'}:
            data = Filters.objects.all()

        else:
            data = Filters.objects.filter(**filter_kwargs)

        if 'decades' in include:
            available_years = list(data.values_list('reference_year', flat=True))
            start_years = sorted(set(10 * (year // 10) for year in available_years))
            decades = [{'name': f"{start}-{start + 9}", 'start': start, 'end': start + 9} for start in start_years]
            if include_all:
                decades = [{'name': 'Tout'}] + decades
            
            results['decades'] = decades


        if 'observedProperties' in include:
            observed_properties = list(data.values_list('observed_property_determinand', flat=True).order_by('observed_property_determinand').distinct())
            observed_properties = [{'name': prop} for prop in observed_properties]
            if include_all:
                observed_properties = [{'name': 'Tout'}] + observed_properties
            
            results['observedProperties'] = observed_properties

        if 'matrix' in include:
            matrices = list(data.values_list('matrix', flat=True).order_by('matrix').distinct())
            matrices = [{'name': mat} for mat in matrices]
            if include_all:
                matrices = [{'name': 'Tout'}] + matrices

            results['matrix'] = matrices

        return Response(results)


class Pipelines(APIView):
    def get(self, request):
            pipelines = PipelineRun.objects.all().order_by('-started_at')
            return Response(PipelineSerializer(pipelines, many = True).data)
    
class GetPipeline(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        pipeline = PipelineRun.objects.get(id = id)
        return Response(PipelineSerializer(pipeline).data)
