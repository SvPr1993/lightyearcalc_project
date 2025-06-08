# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
import json
from app_calc.forms import DataCalcForm


def first_page(request):
    if request.method == 'POST':
        form = DataCalcForm(request.POST)
        if form.is_valid():
            planet_name = form.cleaned_data["planet_name"]
            destination_sum = form.cleaned_data["destination_sum"]
            full_data = json.dumps({"1": planet_name, "2": destination_sum})
            print(full_data)
            answer_text = f'Расстояние до планеты {planet_name} равно {destination_sum} световым годам'
            return JsonResponse(answer_text, safe=False)
    else:
        form = DataCalcForm()
    return render(request, "../templates/index.html", {'form': form})


