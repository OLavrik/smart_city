import pandas

names_list = ('Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu.csv', 
            'Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu__1-kanalizatsia.csv',
            'Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu_1.csv',
            'Investitsii_v_obekty_intellektualnoy_sobstvennosti_po_2013.csv',
            'Zatraty_na_meropriatia_po_energosberezheniyu.csv',
            'Zatraty_na_meropriatia_po_energosberezheniyu_1.csv',
            'Zatraty_na_meropriatia_po_energosberezheniyu_1-kanalizatsia.csv')

def leave_first(string):
    return string.split(' ', 1)[0]

def remove_first(string):
    return string.split(' ', 1)[1]

def load_df_from_gks(name=names_list[0]):
    data = pandas.read_csv(name)
    data.rename(columns={data.columns[0]: 'headers'}, inplace=True)
    columns = [x.split(' ', 1)[0] for x in data.columns.values]
    data.columns = columns
    return data

def remove_index(data):
    data['headers'] = data['headers'].apply(remove_first)
    return data


if __name__ == "__main__":
    file = names_list[0]
    data = load_df_from_gks(name=file)
    data = remove_index(data)


    print(data)
