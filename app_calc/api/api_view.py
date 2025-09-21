from openai import OpenAI
from rest_framework.response import Response
from rest_framework.views import APIView

from app_calc.api.service import planet_service
from app_calc.models import DataCalc


class CheckPlanet(APIView):
    def get(self, request, planet):
        clean_string = planet.lstrip().rstrip()
        upper_string = clean_string.upper()
        planet_distance = planet_service(upper_string)
        if not planet_distance:
            return Response({"message": "Такой планеты нет"})

        return Response({upper_string: planet_distance})

# сделать шаблонизатор, ошибку сделать прямо в форме отправки, по хорошему подсветить поле с ошибкой
# подключить проект к Docker по принципу предыдущего проекта+
# Разделить код на вью, сервис и репозитории
# Нужно дописать репозиторий, чтобы он взаимодействовал с другими файлами
# Подключить фронт к view planet service
