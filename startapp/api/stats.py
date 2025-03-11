from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, Count, Avg, Min, Max

from collections import Counter

from startapp.models import CountryStats, DashboardData

class GeneralInfo(APIView):
    def get(self, request):
        country_code = request.query_params.get('country_code', '')

        data = CountryStats.objects.filter(iso_alpha2 = country_code)
        
        return Response({
            'Total des sites surveillés': data.values_list('total_monitoring_sites', flat=True).first(),
            'Décennies': data.values_list('decades_covered', flat=True).first(),
            'Catégorie des corps d\'eau' : data.values_list('water_body_category', flat=True).first(),
            'Matrice': data.values_list('matrix', flat=True).first(),
            'Total des propriétés observées': data.values_list('count_of_chemicals_monitored', flat=True).first(),
            'Total des échantillons collectés': data.values_list('number_of_collected_samples', flat=True).first(),
            'Taux d\'échantillons confirmés': data.values_list('proportion_of_confirmed_samples', flat=True).first(),
            'Le déterminant le plus observé': data.values_list('most_monitored_determinand', flat=True).first(),
            'Concentration Moyenne': data.values_list('mean_concentration', flat=True).first(),
            'Valeur minimale mesurée': data.values_list('minimum_recorded_value', flat=True).first(),
            'Valeur maximale mesurée': data.values_list('maximum_recorded_value', flat=True).first(),
            'Écart type des données': data.values_list('standard_deviation', flat=True).first(),
            'Nombre total d\'échantillons': data.values_list('total_samples', flat=True).first(),
            'Unité de Mesure': data.values_list('unit_of_measure', flat=True).first()
        })

        
class GetDashBoardData(APIView):
    def post(self, request):
        filter_kwargs = request.data.get('filter_kwargs', {})
        filter_kwargs = {key: value for key, value in filter_kwargs.items() if value != "Tout"}
        
        if not isinstance(filter_kwargs, dict) or filter_kwargs == {}:
            queryset = DashboardData.objects.all()
        else :
            queryset = DashboardData.objects.filter(**filter_kwargs)
            
        if queryset.values().count() > 0:   
            yearly_data = queryset.values("reference_year").annotate(avg_value=Avg("result_mean_value")).order_by("reference_year")
            all_determinand_stats = (
                queryset
                .values("observed_property_determinand")
                .annotate(
                    total_samples=Sum("number_of_collected_samples"),
                    avg=Avg("result_mean_value"),
                    min=Min("result_minimum_value"),
                    max=Max("result_maximum_value"),
                    uom=Min("uom")
                )
                .order_by("-total_samples")
            )

            top_5_observed_determinand = list(all_determinand_stats[:5]) 
            
            water_body_categories = queryset.values_list("list_of_water_body_category", flat=True)
            category_counts = Counter()
            for row in water_body_categories:
                if row: 
                    category_counts.update(row.split(", "))
                            
            return Response(
                {
                    'count_chemicals_monitored': queryset.aggregate(Count('observed_property_determinand', distinct=True))['observed_property_determinand__count'],
                    'count_monitoring_sites': len(set(monitoring_site for sublist in queryset.values_list('list_of_monitoring_sites', flat=True) for monitoring_site in sublist.split(', '))),
                    'number_of_collected_samples': queryset.aggregate(Sum('number_of_collected_samples'))['number_of_collected_samples__sum'],
                    'proportion_of_confirmed_samples': (
                        (queryset.aggregate(Sum('nominator_of_confirmed_samples'))['nominator_of_confirmed_samples__sum'] or 0) /
                        (queryset.aggregate(Sum('denominator_of_confirmed_samples'))['denominator_of_confirmed_samples__sum'] or 0)
                    ) if queryset.aggregate(Sum('denominator_of_confirmed_samples'))['denominator_of_confirmed_samples__sum'] else 0,
                    'loq_donut': {
                        'data': [
                            queryset.aggregate(Sum('under_loq'))['under_loq__sum'] or 0,
                            queryset.aggregate(Sum('above_loq'))['above_loq__sum'] or 0
                        ],
                        'labels': ['En dessous de LOQ', 'Au dessus de LOQ'],
                    },
                    'property_line': [{"x": str(year["reference_year"]), "y": round(year["avg_value"], 2)} for year in yearly_data],
                    'property_bar': [{"x": item["observed_property_determinand"], "y": item["total_samples"]} for item in top_5_observed_determinand],
                    'determinand_table': [
                        {
                            "determinand": item["observed_property_determinand"],
                            "total_samples": item["total_samples"],
                            "mean": round(item["avg"], 2) if item["avg"] is not None else 0,
                            "min": item["min"],
                            "max": item["max"],
                            'uom' : item["uom"]
                        } for item in all_determinand_stats
                    ],
                    'waterbody_table' : [
                        {
                            "category": category, 
                            "number": count
                        } for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)]
                }
            )
        else :
            return Response(status=204)

        