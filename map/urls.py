from django.urls import path
#from .views import 

app_name = "nycmap"

urlpatterns = [
    path("", map, name="nycmap")
]
