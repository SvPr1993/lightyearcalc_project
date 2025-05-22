from django.shortcuts import render


class UserInput:
    planet_name = input(str("Введите название планеты: "))
    distination_sum = int(float("Введите количество световых лет до планеты: "))
