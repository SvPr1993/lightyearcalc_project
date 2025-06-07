from django.db import models


class DataCalc(models.Model):
    planet_name = models.CharField(max_length=100)
    destination_sum = models.IntegerField()
