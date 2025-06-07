# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json
from app_calc.forms import DataCalcForm


def first_page(request):
    if request.method == 'POST':
        form = DataCalcForm(request.POST)
        if form.is_valid():
            planet_name = form.cleaned_data["planet_name"]
            destination_sum = form.cleaned_data["destination_sum"]
            full_data = json.dumps({"1": planet_name, "2": destination_sum})
            return JsonResponse(full_data, safe=False)
    else:
        form = DataCalcForm()
    return render(request, "../templates/index.html", {'form': form})


