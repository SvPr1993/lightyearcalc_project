from app_planets.models import PlanetInfos


def planet_info_repo(planet_name: str):
    try:
        results = PlanetInfos.objects.filter(planet_name__icontains=planet_name).last()
        return results.destination_sum
    except:
        return None


def destination_sum_repo():
    one_light_year_km = 9460730472580.8
    return one_light_year_km
