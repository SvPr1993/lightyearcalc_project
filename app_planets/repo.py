from app_planets.models import PlanetInfos


def planet_info_repo(planet_name: str):
    try:
        results = PlanetInfos.objects.filter(planet_name__icontains=planet_name).last()
        return results.destination_sum
    except Exception as e:
        print("++++++++++++++EX", e)
        raise e


