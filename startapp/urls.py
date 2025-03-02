from django.urls import path
from . import api
urlpatterns = [
    path("water-quality/general-info/", api.GeneralInfo.as_view(), name="general_info"),
]
