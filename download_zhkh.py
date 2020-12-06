import sys

import pandas as pd
import requests
import json
import pandas as pd

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
    "ямало": "Ямало-Ненецкий АО",
    "ненецкий": "Ненецкий АО",
    "тульская": "Тульская область"
}

titles_mapping = {
    'COLD_WATER': "Оснащенность многоквартирных домов общедомовыми приборами учета холодной воды",
    'HOT_WATER': "Оснащенность многоквартирных домов общедомовыми приборами учета горячей воды",
    'ELECTRICITY': "Оснащенность многоквартирных домов общедомовыми приборами учета электроэнергии",
    'THERMAL_ENERGY': "Оснащенность многоквартирных домов общедомовыми приборами учета теплоносителя"
}

columns_mapping = {
    'territory': "Город",
    'housesWithServiceType': "Кол-во подключенных домов",
    'housesWithDevices': "Кол-во оснащенных домов",
    'percentHouseWithDevices': "Процентная составляющая"
}

columns_russian = ["Город", "Кол-во подключенных домов", "Кол-во оснащенных домов", "Процентная составляющая"]

def download_resource(label):
    print(f"Downloading resource")
    headers = {'Content-Type': 'application/json;charset=UTF-8', }
    data = '{"withFederalDistricts":false,"serviceType":"' + f'{label}' + '","territories":[],"territoryCategory":"ADMINISTRATIVE","operationYearFrom":1700,"operationYearTo":2020}'

    response = requests.post('https://dom.gosuslugi.ru/interactive-reports/api/rest/services/commonMetersReport/table',
                             headers=headers, data=data)
    resource = response.json()
    return resource


def convert_resource(resource, sphere_name):
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
    return {'columns': columns_russian, 'data': data}


for label in ['COLD_WATER', 'HOT_WATER', 'ELECTRICITY', 'THERMAL_ENERGY']:
    resource = download_resource(label)
    dictionary = convert_resource(resource, label.lower())

    data = pd.DataFrame(data=dictionary["data"], columns=dictionary["columns"])

    def f(former_name):
        lower = former_name.lower()
        for key in REG_MAPPING.keys():
            if key in lower:
                return REG_MAPPING[key]
        print(f"Failed to map {former_name}")
        return pd.NA

    data[columns_mapping['territory']] = data[columns_mapping['territory']].apply(f)
    data = data.groupby(columns_mapping['territory']).sum().reset_index()
    di = data.to_dict(orient='split')
    del di['index']
    
    res = {}
    res['tag'] = "zhkh_" + label.lower()
    res['title'] = titles_mapping[label]
    res.update(di)

    with open(f"./json_data/zhkh_{label}.json", 'wt', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
