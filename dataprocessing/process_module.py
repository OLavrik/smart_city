import pandas

def remove_first(string):
    return string.split(' ', 1)[1]

def convert_city_to_region():
    df = pandas.read_csv('../population.csv')
    df['City'] = df['City'].apply(remove_first)
    print(len(df[df['City'] == 'Москва']['Region']))


if __name__ == '__main__':
    convert_city_to_region()