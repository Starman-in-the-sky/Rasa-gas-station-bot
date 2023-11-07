import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet


class ActionCreateRoute(Action):

    def name(self) -> Text:  # регистрируем имя действия
        return "action_create_route"

    def run(self, dispatcher, tracker, domain):
        from_place = "Химки, Московская область"
        to_place = tracker.get_slot('station_company_name')

        # Отправка запроса к API Yandex Maps для получения маршрута
        response = requests.get(
            f"https://api-maps.yandex.ru/2.1/?apikey=6e08bccf-7da4-46e3-9623-a5ddfd850be6&lang=ru_RU&mode=routes&from={from_place}&to={to_place}")
        route = response.json()['response']['route'][0]['steps']

        # Отправка ответа пользователю
        route_info = ""
        for step in route:
            route_info += step['instruction'] + "\n"
        dispatcher.utter_message(template="utter_route", text=f"Маршрут от Химок до {to_place}:\n{route_info}")

        return [SlotSet("route_info", route_info)]
