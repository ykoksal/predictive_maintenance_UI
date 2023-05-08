from flask import Flask, render_template, render_template_string
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as opy
import json

app = Flask(__name__)


@app.route('/')
def ana_sayfa():
    return render_template('home.html')


@app.route('/hat_duruslari')
def hat_duruslari():
    return render_template('index.html')


@app.route('/dashboard_v2/<machine>')
def dashboard_v2(machine):
    if machine == "MTP101":
        df = pd.read_csv("static/dist/pd/MTP101.csv")
        df["date"] = pd.to_datetime(df["date"])
        df = df.loc[df["date"] <= np.datetime64("2023-02-04T13:13:00")]
    elif machine == "MTP102":
        df = pd.read_csv("static/dist/pd/MTP102.csv")
        df["date"] = pd.to_datetime(df["date"])
        df = df.loc[(df["date"] >= np.datetime64("2023-02-07T16:05:00"))
                    & (df["date"] <= np.datetime64("2023-02-22T03:29:00"))]
    else:
        return "Invalid Data", 400

    data_json = df.to_json(orient="records")
    columns = df.columns[1:-1].tolist()
    return render_template('index2.html', data_json=data_json, columns=columns, machine=machine)


@app.route('/dashboard_v3/<machine>')
def dashboard_v3(machine):
    if machine == "MTP101":
        df = pd.read_excel("static/dist/pd/MTP101_ariza.xlsx")
    elif machine == "MTP102":
        df = pd.read_excel("static/dist/pd/MTP102_ariza.xlsx")
    else:
        return "Invalid Data", 400
    df["date"] = pd.to_datetime(df["date"])
    data_json = json.dumps(json.loads(df.to_json(orient="records")), ensure_ascii=False)
    columns = df.columns[1:].tolist()
    return render_template('index3.html', data_json=data_json, columns=columns, machine=machine)


@app.route('/dashboard_v41')
def dashboard_v41():
    df = pd.read_excel("static/dist/pd/export_operator_genel.xlsx")
    data_json = json.dumps(json.loads(df.to_json(orient="records")), ensure_ascii=False)
    return render_template('index41.html',
                           data_json=data_json,
                           columns='Genel Skorlama',
                           )


@app.route('/dashboard_v42')
def dashboard_v42():
    df = pd.read_excel("static/dist/pd/operator_aylik_merged.xlsx")
    df["date"] = pd.to_datetime(df["date"])
    data_json = json.dumps(json.loads(df.to_json(orient="records")), ensure_ascii=False)

    return render_template('index42.html',
                           data_json=data_json,
                           columns='Aylık Hata Oranı',
                           )
@app.route('/dashboard_v5')
def dashboard_v5():
    return render_template('index5.html')


if __name__ == '__main__':
    app.run(debug=True)
