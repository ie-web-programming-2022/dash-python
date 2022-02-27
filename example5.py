import pandas as pd
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("bike-accidents.csv")
df["HORA"] = df["HORA"].map(lambda time: int(time.split(":")[0]))

app = Dash(__name__)

districts = [{"label": district, "value": district} for district in  df["DISTRITO"].unique()]

app.layout = html.Div(children = [
    html.H1("Bicimad accidents"),
    dcc.Dropdown(
        id="district",
        options=districts,
        value=districts[0]["value"]
    ),
    html.H2("By time of day"),
    dcc.Graph(
        id="by-time",
        figure={
            "data": [],
            "layout": {
                "title": "By time"
            }
        }
    ),
    html.H2("By genre"),
    dcc.Graph(
        id="by-genre",
        figure={
            "data": [],
            "layout": {
                "title": "By genre"
            }
        }
    )
])

xs = list(sorted(df["HORA"].unique()))

@app.callback(
    Output(component_id="by-time",component_property="figure"),
    [Input(component_id="district", component_property="value")]
)
def update_by_time(district):
    my_df = df[df["DISTRITO"] == district]
    hours = my_df["HORA"].value_counts().to_dict()

    values = []

    for hour in range(0, 24):
        if hour in hours:
            values.append(hours[hour])
        else:
            values.append(0)

    figure = go.Figure(
        data = [
            go.Scatter(
                x = list(range(0, 24)),
                y = values
            )
        ]
    )

    return figure


@app.callback(
    Output(component_id="by-genre",component_property="figure"),
    [Input(component_id="district", component_property="value")]
)
def update_by_genre_and_role(district):
    my_df = df[df["DISTRITO"] == district]
    figure = px.bar(my_df, x="SEXO", y="TIPO PERSONA", color="TIPO PERSONA")

    return figure


app.run_server()