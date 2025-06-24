# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from app_calc.service import count_years


def index(request):
    return render(request, "index.html")


def post_data_forms(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number = request.POST.get("number")
        result = count_years(number)
        print(result)
        answer = f"До планеты {name} расстояние равно {result} световых лет"
        return render(request, "index.html", {"result": answer})
    else:
        return redirect("index.html")


def valid_data(request):
    int_result = count_years
    if int_result is not int:
        return render(request, "error.html")
    else:
        pass

# Сделать так чтобы в случае ввода неверных данных обрабатывались ошибки если введены некорректные данные
# Сделать модель для планет солнечной системы и ввести расстояния для планет внести данные в базу данных (сделать лучше другой проект)
# Сделать API и проверить в постмане как как работает
