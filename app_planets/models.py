from django.core.exceptions import ValidationError
from django.db import models
import unicodedata


class PlanetInfos(models.Model):
    planet_name = models.CharField(max_length=100, unique=True)
    destination_sum = models.BigIntegerField()
    weight_planet = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.planet_name}'

    def save(self, *args, **kwargs):
        self.planet_name = unicodedata.normalize('NFKC', self.planet_name).upper().strip()

        super().save(*args, **kwargs)


    # @property
    # def name_display(self):
    #    return unicodedata.normalize('NFKC', self.planet_name).upper()
