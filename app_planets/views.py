# -*- coding: utf-8 -*
from django.shortcuts import render, redirect

from app_planets.service import planets_info_service


def planet_info_views(request):
    if request.method == 'POST':
        planet_name = request.POST.get("name")
        try:
            planets_distance = planets_info_service(planet_name)
            answer = f"До планеты {planet_name} расстояние равно {planets_distance} световых лет"
            return render(request, "app_planets/planets_info.html", {"result": answer})
        except:
            return redirect("error")

    else:
        return render(request, "app_planets/planets_info.html")


def error(request):
    return render(request, "error.html")

# Написать форму, чтобы оно брало из базы данных или написать формулу для посчета
# Если планеты нет в базе и пользователь заполнил данные в форме она выводит либо из базы либо считает
# Нужно в это приложение наш API
# Прочитать про концепцию DDD
# После проверки работы приложение удалить весь лишний код и приложения
# Перетащить в docker postgres
# Нужно убрать из докера django, оставить только postgres