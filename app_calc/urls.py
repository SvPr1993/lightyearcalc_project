from django.urls import path

from app_calc.views import input_data

urlpatterns = [
    path("", input_data),
]
