import requests


def create_route(origin, destination):
    routing_url = "https://api.routing.yandex.net/v2.1/router"
    params = {
        "apikey": "5941ca0f-88a5-462a-b68b-049e98bd248c",
        "format": "json",
        "origin": origin,
        "destination": destination,
        "lang": "ru_RU",
        "routing_mode": "fastest",
        "transit_visibility": "none",
        "vehicle_type": "car",
    }
    response = requests.get(routing_url, params=params).json()
    route_info = response["routes"][0]["legs"][0]
    return route_info