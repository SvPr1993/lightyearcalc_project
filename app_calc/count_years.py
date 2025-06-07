# -*- coding: utf-8 -*-
from app_calc.views import input_data


def count_years():
    sum = input_data()
    full_sum = sum * 9, 460730472580
    return full_sum
