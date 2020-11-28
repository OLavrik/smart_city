import pandas as pd
import pandas as pd
import numpy as np
import matplotlib

import plotly
import plotly.offline as py
import plotly.graph_objs as go

def create_plot():
    df = pd.read_csv('/Users/Olga.Lavrichenko/Documents/Smart_City/smart_city/dataprocessing/gks/Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu__1-kanalizatsia.csv')
    df = df.dropna()
    df = df.sort_values(by='2018 г.', ascending=True)
    x=df["Unnamed: 0"].values

    y=df["2018 г."].values
    data = go.Data([
        go.Bar(
            y=x,
            x=y,
            orientation='h'
        )])
    layout = go.Layout(
        height=1000,
        margin=go.Margin(l=300),
        title="Выделенные финансы на энергосбережение"
    )
    fig = go.Figure(data=data, layout=layout)
    fig.write_image("fig1.pdf")
    py.plot(fig)

def make_save_pdf(path=""):
    df = pd.read_csv('/Users/Olga.Lavrichenko/Documents/Smart_City/smart_city/dataprocessing/gks/Ekonomia_ot_provedennykh_meropriatiy_po_energosberezheniyu__1-kanalizatsia.csv')
    df = df.dropna()
    df.head()
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
    with open("filename.html", "w", encoding="utf-8") as file:
        file.write(html)


if __name__ == '__main__':
    create_plot()