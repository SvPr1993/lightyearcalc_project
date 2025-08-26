from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("app_calc.api_urls")),
    path("", include("app_calc.urls")),
]
