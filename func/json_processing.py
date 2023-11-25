import json
import requests
def making_json():
    path = 'E:\Rasa-bot\Rasa-gas-station-bot\webscrapping\gasscrapping\gasscrapping\spiders\gasPrices.json'
    with open(path, 'r', encoding='utf-8') as input_file:
        data = json.load(input_file)

    new_data = [entry for entry in data if entry.get('address') is not None]

    for entry in new_data:
        if entry.get('station-name') is None:
            entry['station-name'] = 'ЗАПРАВКА'

    with open('output.json', 'w', encoding='utf-8') as output_file:
        json.dump(new_data, output_file, indent=4, ensure_ascii=False)

    input_file.close()
    output_file.close()
