# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
import json


def input_data(request):
    planet_name = input("Введите название планеты: ")
    destination_sum = input("Введите количество световых лет до планеты: ")
    full_data = json.dumps({"1": planet_name, "2": destination_sum})
    return JsonResponse(full_data, safe=False)
