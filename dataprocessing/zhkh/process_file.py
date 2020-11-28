import pandas

names_list = ('tab9.csv', 'tab12.csv')

def load_df_from_zhkh(name=names_list[0]):
    print(name)
    data = pandas.read_csv(name)
    # data.rename(columns={data.columns[0]: 'region'}, inplace=True)
    print(data.head(7))
    return data
    
def mysplit(string):
    return string.split(' ', 1)[1]


def remove_index(data):
    data['city'] = data['city'].apply(mysplit)
    return data


if __name__ == "__main__":
    data = load_df_from_zhkh()
    # data = remove_index(data)
    # data = pandas.read_csv('tab9.csv')
    # print(data['Сведения о количестве персональных компьютеров в образовательных организациях высшего образования по субъектам Российской Федерации '])
    
