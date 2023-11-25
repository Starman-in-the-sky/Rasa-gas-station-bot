import json
from math import sqrt
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from func.json_processing import making_json
from decimal import Decimal


class ActionGreeting(Action):
    def name(self) -> Text:
        return "happy_greeting"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            SlotSet("user_coordinates", [float(55.838369), float(37.483113)])
            # making_json()
            dispatcher.utter_message(text=f"Приветствую, для начала работы пожалуйста введите свой адрес в формате: «Мой адрес: ваш адрес» ")

        except Exception as inst:
            dispatcher.utter_message(text=f"Произошла ошибка при работе бота  Тип исключения: {type(inst)}  Аргументы исключения: {inst.args}  Исключение: {inst}")
            print(f"Тип исключения: {type(inst)}")
            print(f"Аргументы исключения: {inst.args}")
            print(f"Исключение: {inst}")

        return []


class ActionParseUserAddress(Action):
    def name(self) -> Text:
        return "parse_address"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            uaddress = tracker.get_slot("user_address")
            # client = Client("6e08bccf-7da4-46e3-9623-a5ddfd850be6")
            # coordinates = client.coordinates(uaddress)

            SlotSet("user_coordinates", "Ленинградское шоссе, 56, Москва, 125212")

            dispatcher.utter_message(text=f"Благодарю! Теперь вы можете посмотреть адреса ближайших заправок, проложить маршрут, узнать цены на бензин и т.д. Что бы вы хотели сделать?")
        except Exception as inst:
            dispatcher.utter_message(text=f"Произошла ошибка при работе бота  Тип исключения: {type(inst)}  Аргументы исключения: {inst.args}  Исключение: {inst}")
            print(f"Тип исключения: {type(inst)}")
            print(f"Аргументы исключения: {inst.args}")
            print(f"Исключение: {inst}")

        return []


class ActionGetPrices(Action):
    def name(self) -> Text:
        return "check_prices"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            path = 'E:\Rasa-bot\Rasa-gas-station-bot\output.json'
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            price_92 = data[0]["price_92"]
            price_95 = data[0]["price_95"]
            price_spbt = data[0]["price_spbt"]
            price_dt = data[0]["price_dt"]

            dispatcher.utter_message(text=f"Цена на Аи-92:{price_92}, цена на Аи-95:{price_95}, цена на Газ-СПБТ:{price_spbt}, цена на ДТ:{price_dt}")

        except Exception as inst:
            dispatcher.utter_message(text=f"Произошла ошибка при работе бота  Тип исключения: {type(inst)}  Аргументы исключения: {inst.args}  Исключение: {inst}")
            print(f"Тип исключения: {type(inst)}")
            print(f"Аргументы исключения: {inst.args}")
            print(f"Исключение: {inst}")

        return []


class ActionGetNearestStations(Action):
    def name(self) -> Text:
        return "check_nearest_stations"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        def calculate_distance(loc1, loc2):
            return sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)
        try:
            path = 'E:\Rasa-bot\Rasa-gas-station-bot\output.json'
            user_location = (37.483113, 55.838369)
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for station in data:
                station['distance'] = calculate_distance(user_location, (station['x'], station['y']))

            # Сортировка заправок по расстоянию
            data.sort(key=lambda x: x['distance'])

            # Выбор трёх ближайших станций
            closest_stations = data[:3]

            # Формирование итогового массива
            result = [{'station-name': station['station-name'], 'address': station['address']} for station in
                      closest_stations]

            dispatcher.utter_message(text=f"Ближайшие заправки: {result[0]['station-name']} по адресу - {result[0]['address']}, {result[1]['station-name']} по адресу - {result[1]['address']}, {result[2]['station-name']} по адресу - {result[2]['address']}")

        except Exception as inst:
            dispatcher.utter_message(text=f"Произошла ошибка при работе бота  Тип исключения: {type(inst)}  Аргументы исключения: {inst.args}  Исключение: {inst}")
            print(f"Тип исключения: {type(inst)}")
            print(f"Аргументы исключения: {inst.args}")
            print(f"Исключение: {inst}")

        return []


class ActionCreateRoute(Action):

    def name(self) -> Text:
        return "create_route"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            from_place = tracker.get_slot("user_address")
            to_place = tracker.get_slot("station_company_name")

            # Создаем URL для маршрута на Яндекс Картах
            route_info = f"https://yandex.ru/maps/?rtext={from_place}~{to_place}&rtt=auto"

            # Отправляем URL пользователю
            dispatcher.utter_message(text=f"Ссылка на маршрут в Яндекс Картах: \"{route_info}\"")

        except Exception as inst:
            dispatcher.utter_message(text=f"Произошла ошибка при создании ссылки")
            print(type(inst))
            print(inst.args)

        return []
