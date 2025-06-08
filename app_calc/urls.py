from django.urls import path
from app_calc import views

urlpatterns = [
    path("", views.index),
    path("postdataforms/", views.post_data_forms),
]
