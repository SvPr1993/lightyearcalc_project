from django.urls import path
from app_calc.api import api_view

urlpatterns = [
    path("distance/<str:planet>", api_view.CheckPlanet.as_view()),
]