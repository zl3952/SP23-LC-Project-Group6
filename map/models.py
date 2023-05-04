import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class NYCData(models.Model):
    unique_id = models.CharField(max_length=30)
    indicator_id = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    measure = models.CharField(max_length=30)
    measure_info = models.CharField(max_length=30)
    geo_type_name = models.CharField(max_length=30)
    geo_join_id = models.CharField(max_length=30)
    geo_place_name = models.CharField(max_length=30)
    time_period = models.CharField(max_length=30)
    start_date = models.TimeField(auto_now=False, auto_now_add=False)
    data_value = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
