from django.urls import path

from app_calc.views import first_page

urlpatterns = [
    path("", first_page),
]
