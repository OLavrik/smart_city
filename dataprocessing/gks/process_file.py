import pandas

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from processing_utils import process_module

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

# Specify file names here
names_list = ('Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu.csv',
              'Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu__1-kanalizatsia.csv',
              'Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu_1.csv',
              'Zatraty_na_meropriatia_po_energosberezheniyu.csv',
              'Zatraty_na_meropriatia_po_energosberezheniyu_1.csv',
              'Zatraty_na_meropriatia_po_energosberezheniyu_1-kanalizatsia.csv')


# Load data from files to dataframe structures
def load_df_from_gks(name=names_list[0]):
    data = pandas.read_csv(name)
    data.rename(columns={data.columns[0]: 'headers'}, inplace=True)
    columns = [x.split(' ', 1)[0] for x in data.columns.values]
    data.columns = columns
    return data


# Remove ids from the citys
def remove_index(data):
    data['headers'] = data['headers'].apply(process_module.remove_first)
    return data


# Replace cities with regions
def substitute_cities(data):
    data['headers'] = process_module.convert_cities_to_regions(data['headers'])
    return data


# Function to create JSON
def create_json(file):
    data = load_df_from_gks(name=file)
    data.fillna(0, inplace=True)
    data = remove_index(data)
    data = substitute_cities(data)

    def f(former_name):
        lower = former_name.lower()
        for key in REG_MAPPING.keys():
            if key in lower:
                return REG_MAPPING[key]
        print(f"Failed to map {former_name}")
        return pandas.NA

    data['headers'] = data['headers'].apply(f)
    # print(data)
    data = data.groupby('headers').sum().reset_index()
    # print(data)
    di = data.to_dict(orient='split')
    del di['index']

    filename = file.split('.', 1)[0]
    with open(f"{filename}.json", 'wt', encoding='utf-8') as f:
        json.dump(di, f, ensure_ascii=False, indent=2)


# Execute creation
if __name__ == "__main__":
    for file in names_list:
        create_json(file)
