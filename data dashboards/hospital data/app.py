""" 
we will visualize the following data in an interactive dashboard:

1. County: scatter plot, no-of deaths, 30-day mortality:30-day readmission
2. cards: Total cases, risk adjusted rate // 30-day-mortality, 30-day-readmission
3. cards: Total deaths cases, combines 30-day readmission and mortality
4. cards: Total cases, combined
5. cards: Total cases all
6. Location : geoplot


"""
from plotly.basedatatypes import _indexing_combinations


try:
    #data analysis modules 
    import pandas as pd
    import numpy as np
    from numpy import int32
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
sum_Risk_Adjusted_Rate = df.groupby(['County'])['Risk Adjusted Rate'].agg('sum').astype(int32)
sum_No_of_Deaths_Readmissions = df.groupby(['County'])['No of Deaths/Readmissions'].agg('sum').astype(int32)
Total_sum_No_of_Deaths_Readmissions = df['No of Deaths/Readmissions'].sum().astype(int32)#sum of No of Deaths/Readmissions
Total_sum_No_of_Cases = df['No of Cases'].sum().astype(int32)#sum of No of Cases
Total_sum_Risk_Adjusted_Rate = df['Risk Adjusted Rate'].sum().astype(int32)#sum of Risk Adjusted Rate
Total_sum_counties_affected = df['County'].count()#sum of counties affected
Unique_Hospital_rating = np.array(df['Hospital Ratings'].unique())#numpy list of uniwue values in the column
Total_sum_Hospital_Ratings = df['Hospital Ratings'].value_counts()#count the number of unique values in the columns

### temporary variables that will be removed 

Alameda_sum = sum_County[0] #alameda county sum county
Alameda_Risk_Adjusted_Rate = sum_Risk_Adjusted_Rate[0]
Alameda_No_of_Deaths_Readmissions = sum_No_of_Deaths_Readmissions[0]

''' 

we define the layout of the app

'''
### we define variables for the figures

### bar chart for county aganist no. cases
values = []
for i in sum_County:
    values.append(i)

pie_data = {'County': counties, 'Values': values}
pie_df = pd.DataFrame(pie_data)
bar = px.bar(pie_df,  x='County', y='Values')

### pie chart for hospital ratings
Value = []
for x in Total_sum_Hospital_Ratings:
    Value.append(x)

bar_data = {'Ratings':Unique_Hospital_rating, 'Values':Value}
bar_df = pd.DataFrame(bar_data)

pie = px.pie(bar_df, values='Values', names='Ratings')
### line chart
dataX = []
dataY = []
dataZ = []
for a in sum_County:
    dataX.append(a)
for b in sum_No_of_Deaths_Readmissions:
    dataY.append(b)
for c in sum_Risk_Adjusted_Rate:
    dataZ.append(c)

scatter_data = {'Counties': counties, 'Totals': dataX, 'Deaths & Readmission': dataY, 'Risk adjusted rate': dataZ }

scatter_df = pd.DataFrame(scatter_data)

scatter = px.scatter(scatter_df, x="Risk adjusted rate", y="Deaths & Readmission",
	         size="Totals", color="Counties",
                 hover_name="Counties", log_x=True, size_max=30)

### setting the layout for the app

app.layout = dbc.Container([
    ##HEADER SECTION
    html.Div([
        html.H6('ISCHAEMIC STROKE DATA', className="header-title"),
        html.P('We visualize Ischaemic stroke data ❤️', className="header-description"),
    ], className="header",
    ),
    ##DETAILS FOR ALL COUNTIES SECTION
    dbc.Row([
        html.H4("Sum of cases", className="header-title title-text2"),
        html.Div([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("Total sum of cases", className="card-title title-text"),
                                html.Hr(),
                                html.P( '{}'.format(Total_sum_No_of_Cases), 
                                    className="card-text number-text",
                                ),
                            ]
                        )
                    ],
                    style={"width": "19rem"},
                ),className="mb-4"
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("Total Risk Adjusted Rate", className="card-title title-text"),
                                html.Hr(),
                                html.P('{} '.format(Total_sum_Risk_Adjusted_Rate),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "19rem"},
                )
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("Deaths & Readmission", className="card-title title-text"),
                                html.Hr(),
                                html.P('{}'.format(Total_sum_No_of_Deaths_Readmissions),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "19rem"},
                )
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("No of counties affected", className="card-title title-text"),
                                html.Hr(),
                                html.P('{}'.format(Total_sum_counties_affected),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "19rem"},
                )
            ),
        ], style={"display": "flex"})
    ]),
    ### END OF DETAILS FOR ALL COUNTIES SECTION
    ## Graphs sections, line $ Bar $ scatter plot
    dbc.Row([
        dbc.Col([
            html.H4("Counties/total sum cases", className="card-title"),
            html.Div(
                dcc.Graph(figure=bar),className='card'
            )
        ],
        style={"width": "25rem"},
        ),
        dbc.Col([
            html.H4("Hospital ratings", className="card-title"),
            html.Div(
                dcc.Graph(figure=pie),className='card'
            )
        ]
        ),
        dbc.Col([
            html.H4("Total/risk adjusted/Death", className="card-title"),
            html.Div(
                dcc.Graph(figure=scatter),className='card'
            )
        ]
        )
    ]),
    ## RESULTS PER COUNTY
    dbc.Row([
        ###START DROPDWON SECTION
        dbc.Col(
            html.Div(
                dcc.Dropdown(
                    id="counties-dropdown",
                    options=[
                        {"label": Counties, "value": Counties}
                        for Counties in counties
                    ],
                    value="Alameda",
                    clearable=False,
                    searchable=False,
                ),className='card'
            )
        ),
    ]),
    dbc.Row([
        html.H4("Cases per county", className="header-title title-text2"),
        ###END OF DROPDOWN SECTION
        html.Div([
            dbc.Col(
            html.Div(id='dd-output-container'),
            ),
            dbc.Col(
                html.Div(id='dd-output-container1'),
            ),
            dbc.Col(
                html.Div(id='dd-output-container2')
            ),
        ], style={"display": "flex"})
    ]),
    ### END OF RESULTS PER COUNTY
    ##FOOTER SECTION
    html.Div([
        html.H6('MADE BY SYN03 👨‍💻', className="footer-text"),
        html.P('Built on dash', className='footer-span'),
    ], className="footer",
    ),
    ### END OF FOOTER SECTION

],fluid=True)
## intialize the dropdown callbacks

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('counties-dropdown', 'value')])

## defining the interaction, will add more content later
def updated_dropdown(value):

    county_sum = sum_County[value]
    return dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4('{} Total cases'.format(value), className="card-title title-text"),
                                html.Hr(),
                                html.P('{} '.format(county_sum),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "25rem"},
                )

@app.callback(
    dash.dependencies.Output('dd-output-container1', 'children'),
    [dash.dependencies.Input('counties-dropdown', 'value')])

## defining the interaction, will add more content later
def updated_dropdown1(value):

    risk_sum = sum_Risk_Adjusted_Rate[value]
    return dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4('{} Risk adjusted rate'.format(value), className="card-title title-text"),
                                html.Hr(),
                                html.P('{} '.format(risk_sum),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "25rem"},
                )

@app.callback(
    dash.dependencies.Output('dd-output-container2', 'children'),
    [dash.dependencies.Input('counties-dropdown', 'value')])

## defining the interaction, will add more content later
def updated_dropdown2(value):

    sum_deaths = sum_No_of_Deaths_Readmissions[value]
    return dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4('{} Deaths & Readmission'.format(value), className="card-title title-text"),
                                html.Hr(),
                                html.P('{} '.format(sum_deaths),
                                    className="card-text number-text",
                                ),
                            ]
                        ),
                    ],
                    style={"width": "25rem"},
                )

###initialize the app
if __name__ == '__main__':
    app.run_server(debug=True)