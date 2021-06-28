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
    from yahoo_fin.stock_info import *
    import yfinance as yf

except Exception as e:
    print(e)



##SETTING THE BOOSTRAP THEME AND TITLE OF WEBSITE
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Live market: S&P live market data"

### DOING SOME WEIRD SHIT





### WE INITIALIZE THE APP
if __name__ == '__main__':
    pass