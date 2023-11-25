import json
from yandex_geocoder import Client
import random
with open("output.json", "r", encoding='utf-8') as file:
    data = json.load(file)

client = Client("c37710ac-56bc-4985-8dec-cae9cf1d5bb5")
for item in data:
    coordinates = client.coordinates(f"{item['address']}")
    item['x'] =float(coordinates[0])
    item['y'] =float(coordinates[1])

with open("output.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)