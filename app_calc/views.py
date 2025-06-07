# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from django.template import loader


def input_data(request):
    template = loader.get_template("index.html")
    planet_name = input("Введите название планеты: ")
    destination_sum = input("Введите количество световых лет до планеты: ")
    full_data = json.dumps({"1": planet_name, "2": destination_sum})
    return JsonResponse(full_data, safe=False)
