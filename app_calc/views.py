# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from app_calc.service import count_years


def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number_str = request.POST.get("number")
        try:
            number = int(number_str)
            result = count_years(number)
            print(result)
            answer = f"До планеты {name} расстояние равно {result} световых лет"
            return render(request, "app_planets/planets_info.html", {"result": answer})
        except:
            return redirect("error")

    else:
        return render(request, "app_planets/planets_info.html")


def error(request):
    return render(request, "error.html")
