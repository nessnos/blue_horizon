from .models import WaterData
from django.db.models import Avg, Max, Min, Count,StdDev, Q

def fetch_general_info(country_code):
    """Retrieve summarized water quality data for a given country code."""

    # Filter data by country code
    queryset = WaterData.objects.filter(country__code=country_code)

    if not queryset.exists():
        return {"error": "No data available for this country."}

    # Compute all statistics in a single query using `aggregate`
    aggregated_data = queryset.aggregate(
        total_sites=Count("monitoring_site_identifier", distinct=True),
        min_year=Min("phenomenon_time_reference_year"),
        max_year=Max("phenomenon_time_reference_year"),
        count_of_chemicals=Count("observed_property_determinand_code", distinct=True),
        total_samples=Count("result_number_of_samples"),
        mean_concentration=Avg("result_mean_value"),
        min_value=Min("result_minimum_value"),
        max_value=Max("result_maximum_value"),
        std_deviation=Avg("result_standard_deviation_value"),
        missing_data_count=Count("result_observation_status", filter=Q(result_observation_status__in=["L", "M", "N", "O"]))
    )

    # Fetch distinct values for water body categories and matrix types
    water_body_categories = list(queryset.values_list("parameter_water_body_category__label", flat=True).distinct())
    matrix_types = list(queryset.values_list("procedure_analysed_matrix__label", flat=True).distinct())

    # Compute missing data percentage
    total_records = queryset.count()
    missing_data_percentage = (aggregated_data["missing_data_count"] / total_records) * 100 if total_records > 0 else 0

    # Prepare the response
    data = {
        "Total Monitoring Sites": aggregated_data["total_sites"],
        "Decades Covered": f"{aggregated_data['min_year']} - {aggregated_data['max_year']}",
        "Water Body Category": water_body_categories if water_body_categories else "N/A",
        "Matrix": matrix_types if matrix_types else "N/A",
        "Count of Chemicals Monitored": aggregated_data["count_of_chemicals"],
        "Number of Collected Samples": aggregated_data["total_samples"],
        "Proportion Of Confirmed Samples": f"{100 - missing_data_percentage:.1f}%",
        "Percentage of Missing Data": f"{missing_data_percentage:.1f}%",
        "Mean Concentration": aggregated_data["mean_concentration"] if aggregated_data["mean_concentration"] is not None else "N/A",
        "Minimum Recorded Value": aggregated_data["min_value"] if aggregated_data["min_value"] is not None else "N/A",
        "Maximum Recorded Value": aggregated_data["max_value"] if aggregated_data["max_value"] is not None else "N/A",
        "Standard Deviation": aggregated_data["std_deviation"] if aggregated_data["std_deviation"] is not None else "N/A"
    }

    return data

def fetch_water_quality_info(country_code):
    """Retrieve water quality statistics for a given country code."""
    # Filter data by country code
    queryset = WaterData.objects.filter(country__code=country_code)

    if not queryset.exists():
        return {"error": "No data available for this country."}

    # Compute all statistics in a single query using `aggregate`
    aggregated_data = queryset.aggregate(
        mean_concentration=Avg("result_mean_value"),
        min_value=Min("result_minimum_value"),
        max_value=Max("result_maximum_value"),
        std_deviation=StdDev("result_standard_deviation_value"),
        total_samples=Count("result_number_of_samples")
    )

    # Find the most monitored determinand
    most_monitored = (
        queryset.values("observed_property_determinand_code__label")
        .annotate(count=Count("observed_property_determinand_code"))
        .order_by("-count")
        .first()
    )

    # Prepare the response
    data = {
        "Most Monitored Determinand": most_monitored["observed_property_determinand_code__label"] if most_monitored else "N/A",
        "Mean Concentration": f"{aggregated_data['mean_concentration']:.3f} µg/L" if aggregated_data["mean_concentration"] is not None else "N/A",
        "Minimum Recorded Value": f"{aggregated_data['min_value']:.3f} µg/L" if aggregated_data["min_value"] is not None else "N/A",
        "Maximum Recorded Value": f"{aggregated_data['max_value']:.3f} µg/L" if aggregated_data["max_value"] is not None else "N/A",
        "Standard Deviation": f"{aggregated_data['std_deviation']:.3f} µg/L" if aggregated_data["std_deviation"] is not None else "N/A",
        "Total Samples": aggregated_data["total_samples"] if aggregated_data["total_samples"] else "N/A",
    }
    return data