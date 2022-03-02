from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import data_requests

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="name", placeholder="Name", value="Nora"),
    dcc.Graph(
        id = "my_graph",
        figure = {}
    )
])

@app.callback(
    Output(component_id="my_graph", component_property="figure"),
    [Input(component_id="name", component_property="value")]
)
def update_message(name):
    data = data_requests.get_mttr_p95(name)

    rows = []
    for row in data:
        rows.append({})

    return {
        "data": rows
    }

app.run_server(debug=True)