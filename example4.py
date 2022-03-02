import pandas as pd
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

df = pd.read_csv("bike-accidents.csv")

app = Dash(__name__)

districts = [{"label": district, "value": district} for district in  df["DISTRITO"].unique()]
kinds_of_accidents = [{"label": kind, "value": kind} for kind in df["TIPO ACCIDENTE"].unique()]

app.layout = html.Div(children = [
    html.H1("Bicimad accidents by district"),
    html.H2("District"),
    dcc.Dropdown(
        id="district",
        options=districts,
        multi=True,
        value=[districts[0]["value"]]
    ),
    html.H2("Kind of accident"),
    dcc.Dropdown(
        id="kind_of_accident",
        options=kinds_of_accidents
    ),
    html.H2("kind of accident"),
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
        Input(component_id="kind_of_accident", component_property="value")
    ]
)
def update(districts, kind_of_accident):
    data = []

    filtered_df = df[df["TIPO ACCIDENTE"] == kind_of_accident]

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

app.run_server(debug=True)
