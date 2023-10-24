import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker

class ActionCreateRoute(Action):

    def name(self) -> Text:  # регистрируем имя действия
        return "action_create_route"

    def run(self, dispatcher, tracker, domain):
        from_place = "Химки, Московская область"
        to_place = tracker.get_slot('station_company_name')

        # Отправка запроса к API Yandex Maps для получения маршрута
        response = requests.get(
            f"https://api-maps.yandex.ru/2.1/?apikey=5941ca0f-88a5-462a-b68b-049e98bd248c&lang=ru_RU&mode=routes&from={from_place}&to={to_place}")
        route = response.json()['response']['route'][0]['steps']

        # Отправка ответа пользователю
        route_info = ""
        for step in route:
            route_info += step['instruction'] + "\n"
        dispatcher.utter_message(template="utter_route", text=f"Маршрут от Химок до {to_place}:\n{route_info}")

        return route_info
