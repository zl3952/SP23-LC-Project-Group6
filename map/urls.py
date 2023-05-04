from django.urls import path
from .views import nyc_data_view
from .models import NYCData

app_name = "nycmap"

urlpatterns = [
    path("", nyc_data_view, name="map"),
]
