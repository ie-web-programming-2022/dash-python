
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children = [
  html.H1("more interesting callbacks!"),
  dcc.Dropdown(
    id="choice",
    options=[
      {"label": "Apple", "value": "AAPL"},
      {"label": "Google", "value": "GOOG"},
      {"label": "Microsoft", "value": "MSFT"},
    ],
    value="GOOG"
  ),
  dcc.Graph(
    id="stock-graph",
    figure={
      "data": [],
      "layout": {
        "title": "Stock prices"
      }
    }
  )
])

stocks = {
  "AAPL": [1, 1.4, 2],
  "GOOG": [4, 1, 2],
  "MSFT": [12, 2, 1]
}

@app.callback(
  Output(component_id="stock-graph",component_property="figure"),
  [Input(component_id="choice", component_property="value")]
)
def change_h2_on_input_change(value):
    return {
      "data": [
        {'x': ["Jan", "Feb", "Mar"], 'y': stocks[value], 'type': 'bar', 'name': value},
      ],
      "layout": {
        "title": "Stock prices"
      }
    }

app.run_server()