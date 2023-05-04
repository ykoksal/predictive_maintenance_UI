from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as opy
app = Flask(__name__)

@app.route('/')
def index():
    # Create sample data
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D'],
        'value': [10, 15, 13, 17]
    })

    # Create a bar chart
    bar_chart = px.bar(data, x='category', y='value')

    # Create a time series chart
    time_series_data = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100, freq='M'),
        'value': (20 + 2 * np.random.randn(100)).cumsum()
    })

    # time_series_chart = px.line(time_series_data, x='date', y='value')

    time_series_chart = go.Figure()
    time_series_chart.add_trace(go.Scatter(x=time_series_data['date'], y=time_series_data['value'], mode='lines'))

    time_series_chart_layout = go.Layout(
        title='Time Series Chart',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Value')
    )
    time_series_chart.update_layout(time_series_chart_layout)

    # Convert the charts to HTML
    bar_chart_html = bar_chart.to_html(full_html=False)
    time_series_chart_html = opy.plot(time_series_chart, auto_open=False, output_type='div')

    return render_template('index.html', bar_chart=bar_chart_html, time_series_chart=time_series_chart_html)

@app.route('/hat_duruslari')
def hat_duruslari():
    # Create sample data
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D'],
        'value': [10, 15, 13, 17]
    })

    # Create a bar chart
    bar_chart = px.bar(data, x='category', y='value')

    # Create a time series chart
    time_series_data = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100, freq='M'),
        'value': (20 + 2 * np.random.randn(100)).cumsum()
    })

    time_series_chart = px.line(time_series_data, x='date', y='value')

    return render_template('index.html', bar_chart=bar_chart.to_html(), time_series_chart=time_series_chart.to_html())

@app.route('/dashboard_v2')
def dashboard_v2():
    # Create sample data
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D'],
        'value': [10, 15, 13, 17]
    })

    # Create a bar chart
    bar_chart = px.bar(data, x='category', y='value')

    # Create a time series chart
    time_series_data = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100, freq='M'),
        'value': (20 + 2 * np.random.randn(100)).cumsum()
    })

    # time_series_chart = px.line(time_series_data, x='date', y='value')

    time_series_chart = go.Figure()
    time_series_chart.add_trace(go.Scatter(x=time_series_data['date'], y=time_series_data['value'], mode='lines'))

    time_series_chart_layout = go.Layout(
        title='Time Series Chart',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Value')
    )
    time_series_chart.update_layout(time_series_chart_layout)

    # Convert the charts to HTML
    bar_chart_html = bar_chart.to_html(full_html=False)
    time_series_chart_html = opy.plot(time_series_chart, auto_open=False, output_type='div')

    return render_template('index2.html', bar_chart=bar_chart_html, time_series_chart=time_series_chart_html)

@app.route('/dashboard_v3')
def dashboard_v3():
    # Create sample data
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D'],
        'value': [10, 15, 13, 17]
    })

    # Create a bar chart
    bar_chart = px.bar(data, x='category', y='value')

    # Create a time series chart
    time_series_data = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100, freq='M'),
        'value': (20 + 2 * np.random.randn(100)).cumsum()
    })

    time_series_chart = px.line(time_series_data, x='date', y='value')

    return render_template('index3.html', bar_chart=bar_chart.to_html(), time_series_chart=time_series_chart.to_html())

if __name__ == '__main__':
    app.run(debug=True)