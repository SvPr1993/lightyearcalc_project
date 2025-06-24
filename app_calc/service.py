# -*- coding: utf-8 -*-


def count_years(number):
    try:
        int_value = int(number)
        full_sum = int_value * 9.460730472580
        print("full_sum", full_sum)
        return full_sum
    except:
        print("Invalid input: Not an integer")
