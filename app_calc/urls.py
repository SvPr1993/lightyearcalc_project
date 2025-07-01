from django.urls import path
from app_calc import views

urlpatterns = [
    path("error/", views.error, name="error"),
    path("", views.index),
]
