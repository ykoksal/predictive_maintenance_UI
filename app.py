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
    elif machine == "MTP102":
        df = pd.read_csv("static/dist/pd/MTP102.csv")
    else:
        return "Invalid Data", 400

    df["date"] = pd.to_datetime(df["date"])
    df = df.loc[df["date"] <= np.datetime64("2023-02-04T13:13:00")]
    data_json = df.to_json(orient="records")
    columns = df.columns[1:-1].tolist()
    return render_template('index2.html', data_json=data_json, columns=columns, machine=machine)

@app.route('/dashboard_v3/<machine>')
def dashboard_v3(machine):
    if machine == "MTP101":
        df = pd.read_excel("static/dist/pd/SAP_data_prediction.xlsx")
    elif machine == "MTP102":
        df = pd.read_excel("static/dist/pd/SAP_data_prediction.xlsx")
    else:
        return "Invalid Data", 400
    df["date"] = pd.to_datetime(df["date"])
    data_json = json.dumps(json.loads(df.to_json(orient="records")), ensure_ascii=False)
    columns = df.columns[1:].tolist()
    return render_template('index3.html', data_json=data_json, columns=columns, machine=machine)

if __name__ == '__main__':
    app.run(debug=True)
