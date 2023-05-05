from flask import Flask, render_template, render_template_string
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as opy

app = Flask(__name__)


@app.route('/')
def ana_sayfa():

    return render_template('home.html')


@app.route('/hat_duruslari')
def hat_duruslari():

    return render_template('index.html')


@app.route('/dashboard_v2')
def dashboard_v2():
    time_series_data = pd.read_csv("static/dist/pd/MTP101_onsagbiyel.csv")
    time_series_data.rename(columns={"101-9": "value"}, inplace=True)
    # time_series_data = pd.read_csv("static/dist/pd/MTP102_onsagbiyel.csv")
    time_series_data["date"] = pd.to_datetime(time_series_data["date"])
    time_series_data = time_series_data.loc[time_series_data["date"] <= np.datetime64("2023-02-04T13:13:00")]
    time_series_chart = go.Figure()
    time_series_chart.add_trace(go.Scatter(x=time_series_data['date'], y=time_series_data['value'], mode='lines'))

    time_series_chart_layout = go.Layout(
        title='Ön Sağ Biyel Sıcaklığı(°C)',
        xaxis=dict(title='Tarih'),
        yaxis=dict(title='Değer')
    )
    time_series_chart.update_layout(time_series_chart_layout)

    # Convert the charts to HTML
    time_series_chart_html = opy.plot(time_series_chart, auto_open=False, output_type='div')

    # Render the template and store it in a variable
    return render_template('index2.html', time_series_chart=time_series_chart_html)


@app.route('/dashboard_v3')
def dashboard_v3():
    # Create a time series chart
    time_series_data = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100, freq='M'),
        'value': (20 + 2 * np.random.randn(100)).cumsum()
    })

    time_series_chart = px.line(time_series_data, x='date', y='value')

    return render_template('index3.html', time_series_chart=time_series_chart.to_html())


if __name__ == '__main__':
    app.run(debug=True)
