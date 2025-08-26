from django.db import models


class DataCalc(models.Model):
    planet_name = models.CharField(max_length=100)
    destination_sum = models.IntegerField()


class Const(models.Model):
    const_float = models.FloatField()
    data_update = models.DateField(auto_now=True)


