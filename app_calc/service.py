# -*- coding: utf-8 -*-
from django.conf import settings

from app_calc.repository import const


def count_years(number):
    number_const = const()
    full_sum = number * number_const
    print("full_sum", full_sum)
    return full_sum

#Улучшить сервис, чтобы он определить планету и посчитать расстояние до планеты
