""" 
we will visualize the following data in an interactive dashboard:

1. County: scatter plot, no-of deaths, 30-day mortality:30-day readmission
2. cards: Total cases, risk adjusted rate // 30-day-mortality, 30-day-readmission
3. cards: Total deaths cases, combines 30-day readmission and mortality
4. cards: Total cases, combined
5. cards: Total cases all
6. Location : geoplot


 """

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
    #plotly modules
    import plotly.express as px 

except Exception as e:
    print(e)
    
##setiing the boostrap theme and adding the title
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Hospital analytics: Ischaemic stroke data"

##data preprocessing
df = pd.read_csv('hospital.csv', index_col=0)
##checking the null values
null_values = df.isnull().sum()
##drop empty county columns
drop_values = ['County', 'OSHPDID', 'Location ', 'Hospital Ratings']
for i in drop_values:
    df.dropna(subset = [i], inplace=True)
###fill columns with mean 
mean_values = ['Risk Adjusted Rate', 'No of Deaths/Readmissions', 'No of Cases']
for i in mean_values:
    df.fillna(value=df[i].mean(), inplace=True)
empty = df.isnull().sum()
###creating new file with the data cleaned
##df.to_csv('new_hospital.csv')

### defining figures to used


### setting the layout for the app

app.layout = dbc.Container([
    ##introduction section
    html.Div([
        html.H6('ISCHAEMIC STROKE DATA', className="header-title"),
        html.P('We visualize Ischaemic stroke data', className="header-description"),
    ], className="header",
    ),
    ##cards section
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    )
                ],
                style={"width": "18rem"},
            ),className="mb-4"
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
    ]),
    ## Graphs sections, line $ Bar $ scatter plot
    dbc.Row([
        dbc.Col(),
        dbc.Col(),
        dbc.Col()

    ]),
    ## Cards will use later
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "25rem"},
            )
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "25rem"},
            )
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.Hr(),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "25rem"},
            )
        ),
    ]),
    ##geoplot section
    dbc.Row([
        dbc.Col(

        )
    ])

],fluid=True)
### initialize callbacks

###initialize the app
if __name__ == '__main__':
    app.run_server(debug=True)