from app_calc.models import DataCalc


def const():
    planet_obj = DataCalc.objects.filter().first()
    response = f'{planet_obj}'
    print(response)
    context = {"data": planet_obj}
    return context
