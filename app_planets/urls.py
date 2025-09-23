from django.urls import path
from app_planets.views import planet_info_views

urlpatterns = [
    path("", planet_info_views, name="planets_info"),
     ]
