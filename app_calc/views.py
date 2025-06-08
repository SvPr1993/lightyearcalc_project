# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json
from app_calc.forms import DataCalcForm


def index(request):
    return render(request, "index.html")


def postdataforms(request):
    name = request.POST.get("name")
    number = request.POST.get("number")
    result = f"До планеты {name}  расстояние равно {number} световых лет"
    print(result)
    return render(request, "index.html", {"result": result})


def first_page(request):
    context = f"Hello"
    return HttpResponse(context)
#    if request.method == 'POST':
#        form = DataCalcForm(request.POST)
#        if form.is_valid():
#            planet_name = form.cleaned_data["planet_name"]
#            destination_sum = form.cleaned_data["destination_sum"]
#            full_data = json.dumps({"1": planet_name, "2": destination_sum})
#            print(full_data)
#            answer_text = f'Расстояние до планеты {planet_name} равно {full_data} световым годам'
#            return JsonResponse(answer_text, safe=False)
#    else:
#        form = DataCalcForm()
#    return render(request, "../templates/index.html", {'form': form})
