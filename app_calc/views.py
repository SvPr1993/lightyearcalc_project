# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json
from app_calc.forms import DataCalcForm


def index(request):
    return render(request, "index.html")


def post_data_forms(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number = request.POST.get("number")
        result = f"До планеты {name}  расстояние равно {number} световых лет"
        print(result)
        return render(request, "index.html", {"result": result})
    else:
        redirect("index.html")

