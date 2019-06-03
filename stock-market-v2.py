import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas_datareader import data as pdr
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Type your stock symbol in the box below:
    '''),
    dcc.Input(id='input', value="", type='text'),
    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id='output-graph' , component_property='children'),
    [Input(component_id='input' , component_property='value')]
    )

def update_graph(ticker):
    start = datetime.datetime(2019, 1, 1)
    end = datetime.datetime.now()
    df = pdr.DataReader(ticker, 'robinhood', start, end)

    return dcc.Graph(
        id='example-graph',
        figure = {
            #data consist of single dict or list of dict
            #
            'data' : [
                {'x': df.index,'y': df.close, 'type':'line', 'name': ticker},
            ],
            'layout': {
                'title': ticker
            }
        })

if __name__ == '__main__':
    app.run_server(debug=False)
