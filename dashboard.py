import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import requests

app = Dash(__name__)

app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=1000 * 60, n_intervals=0),
    html.H1("Fraud Detection Dashboard"),
    dcc.Graph(id='graph1'),  # Line chart: Fraud trend over time
    dcc.Graph(id='graph2'),  # Bar chart: Fraud by device type
    dcc.Graph(id='graph3'),  # Bar chart: Fraud by region
    dcc.Graph(id='graph4'),  # Bar chart: Daily fraud counts
])

@app.callback(
    [Output('graph1', 'figure'), Output('graph2', 'figure'), Output('graph3', 'figure'), Output('graph4', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n_intervals):
    base_url = 'http://localhost:5002'
    try:
        # Fetch fraud over time
        over_time_resp = requests.get(f'{base_url}/api/fraud_over_time').json()
        print("Fraud Over Time Response:", over_time_resp)  # Debug
        dates = [record['date'] for record in over_time_resp]
        fraud_counts = [record['count'] for record in over_time_resp]

        # Fetch fraud by device type
        device_type_resp = requests.get(f'{base_url}/api/fraud_by_device_type').json()
        print("Device Type Response:", device_type_resp)  # Debug
        device_types = [record['device_type'] for record in device_type_resp]
        device_counts = [record['count'] for record in device_type_resp]

        # Fetch fraud by geography (regions)
        geo_resp = requests.get(f'{base_url}/api/fraud_by_geography').json()
        print("Geography Response:", geo_resp)  # Debug
        regions = [record['country'] for record in geo_resp]
        region_counts = [record['count'] for record in geo_resp]

        # Create figures
        line_fig = px.line(x=dates, y=fraud_counts, title="Fraud Trend Over Time")
        bar_fig1 = px.bar(x=device_types, y=device_counts, title="Fraud by Device Type")
        bar_fig2 = px.bar(x=regions, y=region_counts, title="Fraud by Region")
        bar_fig3 = px.bar(x=dates, y=fraud_counts, title="Daily Fraud Counts")

        return line_fig, bar_fig1, bar_fig2, bar_fig3
    except Exception as e:
        print(f"Error in dashboard update: {e}")
        empty_fig = go.Figure()
        empty_fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        return empty_fig, empty_fig, empty_fig, empty_fig

if __name__ == '__main__':
    app.run_server(debug=True, port=5003)