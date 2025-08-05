# -*- coding: utf-8 -*-
import requests
from django.http import request
from django.shortcuts import render
from django.conf import settings
from app_calc.models import Const
import requests


def const():
    data = Const.objects.filter().last()
    response = f'{data}'
    print(response)
    context = {"data": data}
    constant = random()
    return constant


def random():
    url = settings.URL
    responsce = requests.get(url)
    json = responsce.json()
    print(json["number"])
    print(type(json["number"]))
    return json["number"]
