
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div(children = [
  html.H1("Using callbacks"),
  dcc.Dropdown(
      id="dropdown",
      options= [
          {"value": "one", "label": "one"},
          {"value": "two", "label": "two"}
      ]),
  html.H2(id="id-changes")
])

@app.callback(
  Output(component_id="id-changes",component_property="children"),
  [Input(component_id="dropdown", component_property="value")]
)
def change_h2_on_input_change(value):
    if value:
        return "the value of the input is: " + value
    else:
        return "no value selected yet"

app.run_server()