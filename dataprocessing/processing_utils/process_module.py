import pandas
from functools import partial

def remove_first(string):
    return string.split(' ', 1)[1]

def leave_first(string):
    return string.split(' ', 1)[0]

def convert_city_to_region(city, df):
    region = df[df['City'] == city]['Region']
    if len(region) != 0:
        return region.values[0]
    else:
        return city

def convert_cities_to_regions(df_input):
    df_translate = pandas.read_csv('../../population.csv')
    df_translate['City'] = df_translate['City'].apply(remove_first)
    fun = partial(convert_city_to_region, df=df_translate)
    return df_input.apply(fun)
