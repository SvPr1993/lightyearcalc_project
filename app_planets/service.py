from app_planets.repo import planet_info_repo


def planets_info_service(planet_name: str):
    distance = planet_info_repo(planet_name)
    return distance
