import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('First Dash App'),
    #dcc graph component
    dcc.Graph(id='example',
            figure = {
            #data consist of single dict or list of dict#
            'data' : [{'x':[1,2,3,4,5],'y':[3,5,7,8,9], 'type':'scatter', 'name':'boats'},
                        {'x':[1,2,3,4,5],'y':[6,2,4,3,1], 'type':'bar', 'name':'cars'}
                                ],
            'layout': {
                'title': 'Basic Dash example'
            }
        })
    ])
    
if __name__ == '__main__':
    app.run_server(debug=True)
