from django.urls import path
from .views import general_info
urlpatterns = [
    path("water-quality/general-info/", general_info, name="general_info"),
    path("water-quality/quality-info/", general_info, name="quality_info"),
]
