from django.urls import path
from app_calc import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error/", views.error, name="error"),
     ]
