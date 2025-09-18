from django.db import models
import unicodedata


class DataCalc(models.Model):
    planet_name = models.CharField(max_length=100, unique=True)
    destination_sum = models.IntegerField()

    def save(self, *args, **kwargs):
        self.planet_name = unicodedata.normalize('NFKC', self.planet_name).upper().strip()

        super().save(*args, **kwargs)

    @property
    def name_display(self):
        return unicodedata.normalize('NFKC', self.planet_name).upper()


class Const(models.Model):
    const_float = models.FloatField()
    data_update = models.DateField(auto_now=True)
