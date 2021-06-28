""" 
** 2 columns

we visualize live stock market data and also get live news
1. live market data (stock list)
2. live news data

"""
#### IMPORTING REQUIRED MODULES
from dash_bootstrap_components.themes import YETI


try:
    #data analysis modules 
    import pandas as pd
    import numpy as np
    #dash modules
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    import dash_bootstrap_components as dbc
    from dash.dependencies import Output, Input
    import plotly.graph_objs as go
    #plotly modules
    import plotly.express as px 
    #some other libraries that will be used
    from yahoo_fin.stock_info import * 
    from pandas_datareader import data as web

except Exception as e:
    print(e)



##SETTING THE BOOSTRAP THEME AND TITLE OF WEBSITE
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Live market: S&P live market data"

### TICKER SYMBOLS TO CSV FILE
ticker = tickers_nasdaq()

#df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color":"#22252B",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Live market", className="display-3 title"),
        html.Hr(),
        html.P(
            "We visualize live market data with dash", className="lead"
        ),
        ### CARD SECTION
        dbc.Card(
                [
                    dbc.CardBody(
                        [
                        ]
                    ),
                ], className='sidebar-card'
            )
            ### END OF CARD SEECTION
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([
    dbc.Row([
        dbc.Col([
            html.H4('Live market data', className='top-title-text'),
        ]),
        dbc.Col([
        html.Div(
            dcc.Dropdown(
                id="ticker-dropdown",
                options=[
                    {"label": Ticker, "value": Ticker}
                    for Ticker in ticker
                ],
                value="AACG",
                clearable=False,
                searchable=False,
                ),className='dropdown'
            ),
        ])
    ]),
    dbc.Row([
        ],id='dd-output-container'),
    dbc.Row([
        ],id='dd-output-container1')

],style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


## we intialize app layout
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('ticker-dropdown', 'value')])

def update_graph(value):
    df = web.DataReader('{}'.format(value), data_source='yahoo', start='01-01-2020')
    
    fig = go.Figure(data=go.Ohlc(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']))
    fig.show()

    return dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dcc.Graph(figure=fig)
                        ]
                    ),
                ], className='card'
            )


### WE INITIALIZE THE APP
if __name__ == '__main__':
    app.run_server(debug=True)