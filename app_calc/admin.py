from django.contrib import admin

from app_calc.models import Const


@admin.register(Const)
class ConstAdmin(admin.ModelAdmin):
    list_display = ("const_float", "data_update")


