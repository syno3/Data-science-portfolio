""" 
** 2 columns

we visualize live stock market data and also get live news
1. live market data (stock list)
2. live news data

"""
#### IMPORTING REQUIRED MODULES
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


except Exception as e:
    print(e)



##SETTING THE BOOSTRAP THEME AND TITLE OF WEBSITE
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Live market: S&P live market data"




SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "border-right": "1px solid white"
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
        dbc.Card(
                [
                    dbc.CardBody(
                        [

                        ]
                    ),
                ], className='card'
            )
        ]),
    dbc.Row([
        dbc.Card(
                [
                    dbc.CardBody(
                        [
                        ]
                    ),
                ],className='card'
            )
        ]),
],style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


### WE INITIALIZE THE APP
if __name__ == '__main__':
    app.run_server(debug=True)