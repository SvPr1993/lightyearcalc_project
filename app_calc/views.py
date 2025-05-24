from django.shortcuts import render


def input_data(request):
    planet_name = input(str("Введите название планеты: "))
    distination_sum = input(float("Введите количество световых лет до планеты: "))
    full_data = planet_name + distination_sum
    return full_data
