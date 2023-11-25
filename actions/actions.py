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

            SlotSet("user_coordinates", "55.838369,37.483113")

            dispatcher.utter_message(text=f"Благодарю! Теперь вы можете посмотреть адреса ближайших заправок, проложить маршрут, узнать цены на бензин и т.д. Что бы вы хотели сделать?")
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
            from_place = tracker.get_slot("user_coordinates")
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
