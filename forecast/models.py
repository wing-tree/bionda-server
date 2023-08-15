from django.db import models


# Create your models here.
class Forecast(models.Model):
    objects = models.Manager()
    base_date = models.CharField(max_length=8)
    base_time = models.CharField(max_length=4)
    nx = models.IntegerField()
    ny = models.IntegerField()
    response = models.JSONField()
