import sys

import requests
import json
import pandas as pd

# url = 'https://showdata.gks.ru/backbone/descriptor'
# resp = requests.get(url, allow_redirects=True)
# rosstat_sources = resp.json()
# with open('rosstat_sources.json', 'wt', encoding='utf-8') as f:
#     json.dump(rosstat_sources, f, indent=2, ensure_ascii=False)


def get_resources_list():
    res_list = []
    with open('rosstat_sources.json', 'rt', encoding='utf-8') as f:
        rosstat_sources = json.load(f)

    for el in rosstat_sources:
        if "-17005" in el:
            res_list.append({"id": el['id'], "title": f"{el.get('-17008')} - {el.get('-17005')} - {el.get('-3')}"})
    return res_list


def list_of_dict_to_list_of_val(d):
    if isinstance(d, list):
        return [list_of_dict_to_list_of_val(x) for x in d]
    else:
        return d.get("db_value")


def dowload_resource(id):
    print(f"Downloading resource with id {id}")
    url = f'https://showdata.gks.ru/x/report/{id}/view/compound/'
    resp = requests.get(url, allow_redirects=True)
    resource = resp.json()
    return resource


def get_lowest_children_list(d):
    if isinstance(d[0], dict) and "children" in d[0]:
        return get_lowest_children_list(d[0]["children"])
    return d


def resource_to_df(resource):
    table_raw = resource["data"]["reportData"]["data"]
    table = list_of_dict_to_list_of_val(table_raw)
    # print(table)
    headers_rows = [x["display_title"] for x in
                    get_lowest_children_list(resource["headers"]["reportHeaders"]["row_header"])]
    headers_col = [x["display_title"] for x in
                   get_lowest_children_list(resource["headers"]["reportHeaders"]["col_header"])]
    # print(headers_rows)
    # print(headers_col)
    df = pd.DataFrame(data=table, index=headers_rows, columns=headers_col)
    return df


res_list = get_resources_list()

with open("resource.json", 'wt', encoding='utf-8') as f:
    json.dump(dowload_resource(273992), f, ensure_ascii=False)

for res_desc in res_list:
    try:
        resource = dowload_resource(res_desc["id"])
        print(f"Processing resource \"{res_desc['title']}\"")
        df = resource_to_df(resource)
        df.to_csv(f"rosstat_files\\{res_desc['title']}.csv", encoding='utf-8')
    except:
        print("Failed")
