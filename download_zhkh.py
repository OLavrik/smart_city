import sys

import requests
import json
import pandas as pd


def dowload_resource(label):
    print(f"Downloading resource")
    headers = {'Content-Type': 'application/json;charset=UTF-8',}
    data = '{"withFederalDistricts":false,"serviceType":"' + f'{label}' + '","territories":[],"territoryCategory":"ADMINISTRATIVE","operationYearFrom":1700,"operationYearTo":2020}'
        
    response = requests.post('https://dom.gosuslugi.ru/interactive-reports/api/rest/services/commonMetersReport/table', headers=headers, data=data)
    resource = response.json()
    return resource


def convert_resource(resource):
    table_raw = resource[0]['children']
    columns = ['territory', 'housesWithServiceType', 'housesWithDevices', 'percentHouseWithDevices']
    data = []
    for area in table_raw:
        indicators = []
        indicators.append(area['territory']['name'])
        indicators.append(area['housesWithServiceType'])
        indicators.append(area['housesWithDevices'])
        indicators.append(area['percentHouseWithDevices'])
        data.append(indicators)
    return {'columns':columns, 'data':data}

for label in ['COLD_WATER', 'HOT_WATER', 'ELECTRICITY', 'THERMAL_ENERGY']:
    resource = dowload_resource('COLD_WATER')
    dictionary = convert_resource(resource)
    with open(f"zhkh_{label}.json", 'wt', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
