import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas_datareader import data as pdr
import datetime as dt

app = dash.Dash()

start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()
print ("Start Date:", start)
print ("End Date:", end)
stock = "TSLA" #all caps
df = pdr.DataReader(stock , 'iex', start, end)
# df.reset_index(inplace=False)
print(df.head())

app.layout = html.Div(children=[
    html.H1(children='Stock Graph'),

    html.Div(children='''
        Making a stock graph!.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
