from django.http import request
from django.shortcuts import render

from app_calc.models import Const


def const():
    data = Const.objects.filter().last()
    context = {"data": data}
    print(data)
    return context
# Дописать загрузку данных из модели
# Сделать динамическое число Const, перенести в settings API_KEY
