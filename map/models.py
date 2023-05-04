from django.db import models

# Create your models here.
class NYCData(models.Model):
	uid = models.CharField(max_length = 30)
	iid = models.CharField(max_length = 30)
	name = models.CharField(max_length = 100)
	measure = models.CharField(max_length = 30)
	measureInfo = models.CharField(max_length = 30)
	geoType =  models.CharField(max_length = 30)
	geoJoinID =  models.CharField(max_length = 30)
	geoName =  models.CharField(max_length = 30)
	timePeriod =  models.CharField(max_length = 30)
	startDate = models.TimeField(auto_now=False, auto_now_add=False)
	value = models.CharField(max_length = 30)
	message = models.CharField(max_length = 100)