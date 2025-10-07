from django.urls import path
from app_planets.views import planet_info_views, destination_sum_views

urlpatterns = [
    path("", planet_info_views, name="planets_info"),
    path("distance/", destination_sum_views, name="destination_sum"),
     ]
