""" 
we will visualize the following data in an interactive dashboard:

1. County: scatter plot, no-of deaths, 30-day mortality:30-day readmission
2. cards: Total cases, risk adjusted rate // 30-day-mortality, 30-day-readmission
3. cards: Total deaths cases, combines 30-day readmission and mortality
4. cards: Total cases, combined
5. cards: Total cases all
6. Location : geoplot


 """

from numpy import int32


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


''' 
we modify the data and deal with empty columns in dataframe and create a new csv file

 '''

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


''' 

we define variables that will be used in the code:
1. list of counties in data
2. list of hospitals in the columns
3. group by 30-day readmission and mortality and get risk adjusted rate
4. group by 30-day readmission and mortality and get no of cases
5. group by 30-day readmission and mortality and get total no of deaths and readmission
6. group by counties and get number of cases in each
7. Calculate hospital rating and get values
8.


 '''
### defining variables in figure to used
counties = np.array(df['County'].unique())##counties in the data
hospitals = np.array(df['Hospital'].unique())
sum_30_day_Risk_Adjusted_Rate = df.groupby(['Measure'])['Risk Adjusted Rate'].agg('sum').astype(int32)#group by the unique values in column and count values in the next column
sum_30_day_No_of_Deaths_Readmissions = df.groupby(['Measure'])['No of Deaths/Readmissions'].agg('sum').astype(int32)#group by the unique values in column and count values in the next column
sum_No_of_Cases = df.groupby(['Measure'])['No of Cases'].agg('sum').astype(int32)#group by the unique values in column and count values in the next column
sum_County = df.groupby(['County'])['No of Cases'].agg('sum').astype(int32)#getting counties with the highest rates of cases
Total_sum_No_of_Deaths_Readmissions = df['No of Deaths/Readmissions'].sum()#sum of No of Deaths/Readmissions
Total_sum_No_of_Cases = df['No of Cases'].sum().astype(int32)#sum of No of Cases
Total_sum_Risk_Adjusted_Rate = df['Risk Adjusted Rate'].sum().astype(int32)#sum of Risk Adjusted Rate
Unique_Hospital_rating = np.array(df['Hospital Ratings'].unique())#numpy list of uniwue values in the column
Total_sum_Hospital_Ratings = df['Hospital Ratings'].value_counts()#count the number of unique values in the columns

''' 

we define the layout of the app

 '''

### setting the layout for the app

app.layout = dbc.Container([
    ##introduction section
    html.Div([
        html.H6('ISCHAEMIC STROKE DATA', className="header-title"),
        html.P('We visualize Ischaemic stroke data ❤️', className="header-description"),
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
        dbc.Col([
            html.H4("Card title", className="card-title"),
            html.Div(
                dcc.Graph(),className='card'
            )
        ],
        style={"width": "25rem"},
        ),
        dbc.Col([
            html.H4("Card title", className="card-title"),
            html.Div(
                dcc.Graph(),className='card'
            )
        ]
        ),
        dbc.Col([
            html.H4("Card title", className="card-title"),
            html.Div(
                dcc.Graph(),className='card'
            )
        ]
        )
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
            ),className="mb-5"
        ),
    ]),
    ##geoplot section
    dbc.Row([
        dbc.Col([
            html.H4("Card title", className="card-title"),
            html.Div(
                dcc.Graph(),className='card'
            )
        ]
        )
    ])

],fluid=True)
### initialize callbacks





###initialize the app
if __name__ == '__main__':
    app.run_server(debug=True)