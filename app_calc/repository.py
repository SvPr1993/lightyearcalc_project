from app_calc.models import Const


def const():
    data = Const.objects.filter().last()
    print(data)
    return 0
# Дописать загрузку данных из модели
# Сделать динамическое число Const, перенести в settings API_KEY
