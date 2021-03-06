import sys

import pandas as pd
import requests
import json
import numpy as np

REG_MAPPING = {
    "москва": "Москва",
    "челябинская": "Челябинская область",
    "орловская": "Орловская область",
    "омская": "Омская область",
    "липецкая": "Липецкая область",
    "курская": "Курская область",
    "рязанская": "Рязанская область",
    "брянская": "Брянская область",
    "кировская": "Кировская область",
    "архангельская": "Архангельская область",
    "мурманская": "Мурманская область",
    "санкт": "Санкт-Петербург",
    "ярославская": "Ярославская область",
    "ульяновская": "Ульяновская область",
    "новосибирская": "Новосибирская область",
    "тюменская": "Тюменская область",
    "свердловская": "Свердловская область",
    "новгородская": "Новгородская область",
    "курганская": "Курганская область",
    "калининградская": "Калининградская область",
    "ивановская": "Ивановская область",
    "астраханская": "Астраханская область",
    "хабаровский": "Хабаровский край",
    "чеч": "Чеченская республика",
    "удмур": "Удмуртская республика",
    "осет": "Республика Северная Осетия",
    "мордов": "Республика Мордовия",
    "карел": "Республика  Карелия",
    "калмык": "Республика  Калмыкия",
    "ингуш": "Республика  Ингушетия",
    "башкор": "Республика Башкортостан",
    "адыг": "Республика Адыгея",
    "крым": "Республика Крым",
    "севастоп": "Севастополь",
    "коми": "Республика Коми",
    "пензенская": "Пензенская область",
    "тамбовская": "Тамбовская область",
    "ленинградская": "Ленинградская область",
    "вологодская": "Вологодская область",
    "костромская": "Костромская область",
    "псковская": "Псковская область",
    "ямало": "Ямало-Ненецкий АО",
    "воронежская": "Воронежская область",
    "чукот": "Чукотский АО",
    "еврей": "Еврейская автономская область",
    "тыва": "Республика Тыва",
    "сахалин": "Сахалинская область",
    "амур": "Амурская область",
    "бурят": "Республика Бурятия",
    "хакас": "Республика Хакасия",
    "кемеровская": "Кемеровская область",
    "алтайский": "Алтайский край",
    "алтай": "Республика Алтай",
    "дагест": "Республика Дагестан",
    "балкар": "Кабардино-Балкарская республика",
    "черкес": "Карачаевая-Черкесская республика",
    "краснодарский": "Краснодарский край",
    "ростовская": "Ростовская область",
    "самарская": "Самарская область",
    "татарстан": "Республика Татарстан",
    "марий": "Республика Марий Эл",
    "чуваш": "Чувашская республика",
    "нижегород": "Нижегородская область",
    "владимирс": "Владимирская область",
    "владимиро": "Владимирская область",
    "московская": "Московская область",
    "калужская": "Калужская область",
    "белгородская": "Белгородская область",
    "забайкальский": "Забайкальский край",
    "приморский": "Приморский край",
    "камчатский": "Камачатский край",
    "магаданская": "Магаданская область",
    "саха": "Республика Саха",
    "красноярский": "Красноярский край",
    "оренбургская": "Оренбургская область",
    "саратовская": "Саратовская область",
    "волгоградская": "Волгоградская область",
    "ставропольский": "Ставропольский край",
    "смоленская": "Смоленская область",
    "тверская": "Тверская область",
    "пермская": "Пермский край",
    "пермский": "Пермский край",
    "ханты": "Ханты-Мансийский АО",
    "томская": "Томская область",
    "иркутская": "Иркутская область",
    "ненецкий": "Ненецскй АО",
    "тульская": "Тульская область"
}


def download_resource(label, index):
    headers = {'Content-Type': 'application/json;charset=UTF-8', }
    data = '{"withFederalDistricts":false,"serviceType":"' + f'{label}' + '","territories":["' + f'{index}' + '"],"territoryCategory":"ADMINISTRATIVE","operationYearFrom":1700,"operationYearTo":2020}'
        
    response = requests.post('https://dom.gosuslugi.ru/interactive-reports/api/rest/services/commonMetersReport/table',
                                    headers=headers, data=data)
    resource = response.json()
    return resource

def convert_resource(resource):
    table_raw = resource[0]['children']
    data = []
    for area in table_raw:
        indicators = []
        indicators.append(area['territory']['name'])
        indicators.append(area['housesWithServiceType'])
        indicators.append(area['housesWithDevices'])
        indicators.append(area['percentHouseWithDevices'])
        data.append(indicators)
    return data

def fun(former_name):
    lower = former_name.lower()
    for key in REG_MAPPING.keys():
        if key in lower:
            return REG_MAPPING[key]
    print(f"Failed to map {former_name}")
    return former_name


columns = ['territory', 'housesWithServiceType', 'housesWithDevices', 'percentHouseWithDevices']
for label in ['COLD_WATER', 'HOT_WATER', 'ELECTRICITY', 'THERMAL_ENERGY']:
    data_array = []
    for x in range(1, 77):
        resource = download_resource(label, str(x).zfill(2))
        area_array = convert_resource(resource)
        name = fun(resource[0]['territory']['name'])
        data_array.append({name:area_array})
    
    dictionary = {'columns': columns, 'data': data_array}
    
    with open(f"zhkh_cities_{label}.json", 'wt', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
