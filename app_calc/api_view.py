from rest_framework.response import Response
from rest_framework.views import APIView

from app_calc.models import DataCalc


class CheckPlanet(APIView):
    def get(self, request, planet):
        clean_string = planet.lstrip().rstrip()
        upper_string = clean_string.upper()
        planet_obj = DataCalc.objects.filter(planet_name=upper_string).first()
        if not planet_obj:
            return Response({"message": "Такой планеты нет"})

        return Response({upper_string: planet_obj.destination_sum})

# добавить планеты в админ панель, чтобы на планеты в солнечной системе выдавали конкретный результат
# сделать шаблонизатор, ошибку сделать прямо в форме отправки, по хорошему подсветить поле с ошибкой
# сделать связь с нейросетью chatGTP API или любой другой
# Сделать чтобы планеты из базы данных небыли чувствительными к регистру (в базе данных одни буквы, на выходе другие)
# Разделить код на вью, сервис и репозитории
