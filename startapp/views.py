from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .services import fetch_general_info, fetch_water_quality_info
@api_view(["GET"])
def general_info(request):
    country_id = request.GET.get("country")
    if not country_id:
        return Response({"error": "Country parameter is required"}, status=400)

    data = fetch_general_info(country_id)
    return Response(data)

@api_view(["GET"])
def quality_info(request):
    country_id = request.GET.get("country")
    if not country_id:
        return Response({"error": "Country parameter is required"}, status=400)

    data = fetch_water_quality_info(country_id)
    return Response(data)
