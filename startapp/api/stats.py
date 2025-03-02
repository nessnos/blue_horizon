from rest_framework.response import Response
from rest_framework.views import APIView
from startapp.services import fetch_info


class GeneralInfo(APIView):
    def get(self, request):
        country_id = request.GET.get("country")
        if not country_id:
            return Response({"error": "Country parameter is required"}, status=400)

        data = fetch_info(country_id)
        return Response(data)