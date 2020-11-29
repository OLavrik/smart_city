import pandas as pd
import pandas as pd
import numpy as np
import matplotlib
import json

import plotly
import plotly.offline as py
import plotly.graph_objs as go

def create_plot(json_data):

    print(json_data)
    title=json_data["title"]
    data=[]
    d={}
    for elem in json_data["data"]:
        towns = [_ for _ in elem.values()][0]
        regions=[_ for _  in  elem.keys()][0]
        d[regions]=towns
        #
        # data.extend(res)
    # f=[_ for _ in [elem for elem in json_data["data"]]]
    #
    # print(df.head)
    # # df = pd.read_csv('/Users/Olga.Lavrichenko/Documents/Smart_City/smart_city/dataprocessing/gks/Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu__1-kanalizatsia.csv')
    # df = df.dropna()
    for index, val in d.items():

        main_column=json_data["columns"][-1]
        df = pd.DataFrame(data=val, columns=json_data["columns"])
        make_save_pdf(df, index)
        df = df.sort_values(by=main_column, ascending=True)
        x=df[json_data["columns"][0]]
        y=df[main_column].values
        data = go.Data([
            go.Bar(
                y=x,
                x=y,
                orientation='h'
            )])
        layout = go.Layout(
            height=1000,
            margin=go.Margin(l=100),
            title=title
        )
        fig = go.Figure(data=data, layout=layout)
        fig.write_image(index+"_distribution.pdf")
        py.plot(fig)
        break

def make_save_pdf(df, label=""):

    html='''
<!DOCTYPE html>
<html >
<meta charset="UTF-8">
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

thead {
  background: #2f2c2c;
  background: #2f2c2c;

}
thead th {
  font-size: 15px;
  font-weight: bold;
  color: #f3ecec;
  text-align: left;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
    '''
    html += df.to_html()
    html+="""
    </html>"""
    with open(label+"_tabel.html", "w", encoding="utf-8") as file:
        file.write(html)


if __name__ == '__main__':
    create_plot()