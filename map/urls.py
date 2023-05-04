from django.urls import path
from .views import maps
from .models import NYCData

app_name = "nycmap"

urlpatterns = [
    path("", maps, name="map"),
]
