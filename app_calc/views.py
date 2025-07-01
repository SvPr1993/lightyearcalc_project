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
            return render(request, "index.html", {"result": answer})
        except:
            return redirect("error")

    else:
        return render(request, "index.html")


def error(request):
    return render(request, "error.html")

# Сделать так чтобы в случае ввода неверных данных обрабатывались ошибки если введены некорректные данные
# Сделать модель для планет солнечной системы и ввести расстояния для планет внести данные в базу данных (сделать лучше другой проект)
# Сделать API и проверить в постмане как как работает
