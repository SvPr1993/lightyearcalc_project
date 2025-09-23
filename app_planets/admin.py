from django.contrib import admin
from app_planets.models import PlanetInfos


@admin.register(PlanetInfos)
class DataCalcAdmin(admin.ModelAdmin):
    list_display = ("planet_name", "destination_sum", "weight_planet", "id")
