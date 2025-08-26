from rest_framework.response import Response
from rest_framework.views import APIView


class CheckPlanet(APIView):
    def get(self, request, planet):
        return Response({planet: "999"})


#добавить планеты в админ панель, чтобы на планеты в солнечной системе выдавали конкретный результат
#сделать шаблонизатор, ошибку сделать прямо в форме отправки, по хорошему подсветить поле с ошибкой