import pandas

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

from processing_utils import process_module

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
    data = data.groupby('headers').sum().reset_index()
    filename = file.split('.', 1)[0]
    di = data.to_dict(orient='split')
    di.pop('index')
    with open(f"{filename}.json", 'wt', encoding='utf-8') as f:
        json.dump(di, f, ensure_ascii=False, indent=2)


# Execute creation
if __name__ == "__main__":
    for file in names_list:
        create_json(file)
