from app_planets.repo import planet_info_repo, destination_sum_repo


def planets_info_service(planet_name: str):
    distance = planet_info_repo(planet_name)
    print("Ответ репозитория", distance)
    return distance


def destination_sum_service(destination_sum: int):
    destination_const_km = destination_sum_repo()
    print(type(destination_const_km), type(destination_sum))
    full_sum_km = destination_sum * destination_const_km
    print("full_sum_km", full_sum_km)
    return full_sum_km
