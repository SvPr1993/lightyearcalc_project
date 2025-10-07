# -*- coding: utf-8 -*
from django.shortcuts import render, redirect

from app_planets.models import PlanetInfos
from app_planets.service import planets_info_service, destination_sum_service


def planet_info_views(request):
    if request.method == 'POST':
        planet_name = request.POST.get("name")
        # Данный код исполняется если планета есть в базе в джанго админ
        planets_distance = planets_info_service(planet_name)
        if planets_distance is not None:
            answer = f"До планеты {planet_name} расстояние равно {planets_distance} световых лет"
            return render(request, "app_planets/planets_info.html", {"result": answer})
        else:
            return redirect("destination_sum")

    else:
        return render(request, "app_planets/planets_info.html")


def destination_sum_views(request):
    print("Сработала вторая вьев,,,,,,,,,,,,,,,,,,,,,")
    if request.method == 'POST':
        destination_sum = request.POST.get("destination_sum")
        int_destination_sum = int(destination_sum)
        new_planets_distance = destination_sum_service(int_destination_sum)
        print(new_planets_distance, "++++++++++++++++")
        answer = f"До планеты {'Планета'} расстояние равно {new_planets_distance} световых лет"
        return render(request, "app_planets/destination_sum.html", {"result": answer})

    else:
        return render(request, "app_planets/destination_sum.html")


def error(request):
    return render(request, "error.html")

# Сделать так чтобы в отевте фигурировала планета из 1 функции
# Обработать случай если вместо цифр вводятся другие типы данных во второй функции
# Показать проект фронт энд проекта space adventure
