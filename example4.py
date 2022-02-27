import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv("bike-accidents.csv")

app = dash.Dash(__name__)

districts = [{"label": district, "value": district} for district in  df["DISTRITO"].unique()]

kinds_of_accidents = []
for kind in df["TIPO ACCIDENTE"].unique():
    kinds_of_accidents.append({"label": kind, "value": kind})

app.layout = html.Div(children = [
    html.H1("Bicimad accidents by district"),
    html.H2("District"),
    dcc.Dropdown(
        id="district",
        options=districts,
        multi=True,
        value=[districts[0]["value"]]
    ),
    html.H2("kind of accident"),
    dcc.Dropdown(
        id="accident-kind",
        options=kinds_of_accidents,
        multi=True,
        value=[kinds_of_accidents[0]["value"]]
    ),
    dcc.Graph(
        id="accidents-graph",
        figure={
            "data": [],
            "layout": {
                "title": "accidents"
            }
        }
    )
])

xs = list(sorted(df["HORA"].unique()))

@app.callback(
    Output(component_id="accidents-graph",component_property="figure"),
    [
     Input(component_id="district", component_property="value"),
     Input(component_id="accident-kind", component_property="value")
     ]
)
def update(districts, kinds_of_accidents):

    data = []
    
    filtered = df["TIPO ACCIDENTE"].isin(kinds_of_accidents)
    filtered_df = df[filtered]

    for district in districts:
        count = filtered_df[filtered_df["DISTRITO"] == district]["HORA"].count()
        row = {'x': list(range(0, 100)), 'y': [count], 'type': 'bar', 'name': district}
        data.append(row)

    return {
        "data": data,
        "layout": {
            "title": "accidents"
        }
    }

app.run_server()
