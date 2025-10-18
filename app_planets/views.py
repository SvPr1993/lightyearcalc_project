# -*- coding: utf-8 -*
from django.shortcuts import render, redirect
from app_planets.service import planets_info_service, destination_sum_service


def planet_info_views(request):
    if request.method == 'POST':
        planet_name = request.POST.get("name")
        # Данный код исполняется если планета есть в базе в джанго админ
        planets_distance = planets_info_service(planet_name)
        if planets_distance is not None:
            answer = f"До планеты {planet_name} расстояние равно {planets_distance} километров"
            return render(request, "app_planets/planets_info.html", {"result": answer})
        else:
            return redirect("destination_sum", planet_name)

    else:
        return render(request, "app_planets/planets_info.html")


def destination_sum_views(request, planet=""):
    print("Сработала вторая вьев,,,,,,,,,,,,,,,,,,,,,")
    print(planet)
    # Данный код срабатывает если планеты не в базе джанго админ
    if request.method == 'POST':
        destination_sum = request.POST.get("destination_sum")
        try:
            int_destination_sum = int(destination_sum)
            new_planets_distance = destination_sum_service(int_destination_sum)
            answer = f"До планеты {planet} расстояние равно {new_planets_distance} километров"
        except:
            message_error = "Вы ввели не число!"
            answer = message_error
        return render(request, "app_planets/destination_sum.html", {"result": answer})

    else:
        return render(request, "app_planets/destination_sum.html", {"planet": planet})


def error(request):
    return render(request, "app_planets/error.html")

# Добавить во второй шаблон поле для планеты, если случай если напрямую там нет введенной планеты, если есть то планета планета там тоже есть+



# ТЗ к сайту:
# Сайт на главной странице должен иметь внешний вид свайперов https://russianspacesystems.ru/
# на сайте должно быть 2 формы отправки в базу данных на определенное количество записей с именами в двух случаях
# на сайте должна быть форма напоминания о событии на почту или мобильный телефон
# на сайте должна быть форма отправки обратной связи с неограниченным вводом текста
# на сайте должен быть поиск записей по сайту
