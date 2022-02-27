#%%

from dash import dcc, html, Dash

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Hello Dash'),
    dcc.Graph(
        id='first-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'bar1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'bar2'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


app.run_server()