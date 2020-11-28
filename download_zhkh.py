import sys

import requests
import json
import pandas as pd

# url = 'https://showdata.gks.ru/backbone/descriptor'
# resp = requests.get(url, allow_redirects=True)
# rosstat_sources = resp.json()
# with open('rosstat_sources.json', 'wt', encoding='utf-8') as f:
#     json.dump(rosstat_sources, f, indent=2, ensure_ascii=False)


def dowload_resource():
    print(f"Downloading resource")
    headers = {'Content-Type': 'application/json;charset=UTF-8',}
    data = '{"withFederalDistricts":false,"serviceType":"COLD_WATER","territories":[],"territoryCategory":"ADMINISTRATIVE","operationYearFrom":1700,"operationYearTo":2020}'
        
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


resource = dowload_resource()
dictionary = convert_resource(resource)
with open(f"zhkh.json", 'wt', encoding='utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=2)
