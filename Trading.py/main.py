# -*- coding: utf-8 -*-

#importing the necessary modules needed for the tasks
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import date
import pandas as pd
from matplotlib import style

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['TSLA','AAPL','AMZN','GOOGL','MSFT','INTC']

# We would like all available data from 01/01/2000 until today.
start_date = '2010-01-01'
today = date.today()

#get the data from yahoo site and display the data
df = pdr.DataReader(tickers, data_source='yahoo', start='2017-01-01', end=today)
df.tail()

#displaying the number and type of columns in the dataframe
df.columns

#get the adjusted price for the Tesla
data_plot = df[('Adj Close',  'TSLA')]

#Get tesla volume
volume_plot = df[('Volume',  'TSLA')]

#adding moving averages to the chart, SMA and EMA

df["SMA1"] = data_plot.rolling(window=50).mean()
df["SMA2"] = data_plot.rolling(window=200).mean()


#aading MACD to the chart

exp1 = data_plot.ewm(span=12, adjust=False).mean()
exp2 = data_plot.ewm(span=26, adjust=False).mean()
macd = exp1-exp2
exp3 = macd.ewm(span=9, adjust=False).mean()

#defining color variables and getting different values

colors = {'red': '#ff207c', 'grey': '#42535b', 'blue': '#207cff', 'orange': '#ffa320', 'green': '#00ec8b', 'white' : '#ffffff'}
plt.rc('figure', figsize=(20, 8))
#subplotting matplotlib

fig, axes = plt.subplots(3, 1, gridspec_kw={'height_ratios': [4, 1, 1]})
fig.tight_layout()
style.use('dark_background')
#starting with the first plot

plot_price = axes[0]
# formatting the labelling to the right side of the graph and adding text

plot_price.yaxis.tick_right()
plot_price.set_ylabel('Price (in USD)', fontsize=14)
plot_price.yaxis.set_label_position("right")
plot_price.yaxis.label.set_color(colors['white'])
plot_price.grid(axis='y', color='gainsboro', linestyle='-', linewidth=0.5)
plot_price.set_axisbelow(False)
#setting figure title as TSLA

fig.suptitle('TSLA', size=36, color=colors['white'], x=0.1, y=0.95)
#plot_price.set_title('closing price \nVolume', loc='left')

#formatting the box layout by removing the top and left side

plot_price.spines['top'].set_visible(False)
plot_price.spines['left'].set_visible(False)
plot_price.spines['left'].set_color(colors['grey'])
plot_price.spines['bottom'].set_color(colors['grey'])

#plot_price.legend(loc='upper left', bbox_to_anchor= (-0.005, 0.95), fontsize=16)

# plotting the content of the first graph including the moving averages

plot_price.plot(data_plot, color=colors['blue'], linewidth=2, label='Price')
plot_price.plot(data_plot, label="close")
plot_price.plot(df['SMA1'], 'g--', label="SMA1")
plot_price.plot(df['SMA2'], 'r--', label="SMA2")
plot_price.legend(loc='upper left', bbox_to_anchor= (0.03, 0.85), fontsize=16)
# plotting volume graph 

plot_vol = axes[1]
#aligning the labelling to the right hand side

plot_vol.yaxis.tick_right()
plot_vol.set_ylabel('Volume', fontsize=14)
plot_vol.yaxis.set_label_position("right")
plot_vol.yaxis.label.set_color(colors['white'])
plot_vol.grid(axis='y', color='gainsboro', linestyle='-', linewidth=0.5)
plot_vol.set_axisbelow(False)
#formatting the box border by removing the top and left

plot_vol.spines['top'].set_visible(False)
plot_vol.spines['left'].set_visible(False)
plot_vol.spines['left'].set_color(colors['grey'])
plot_vol.spines['bottom'].set_color(colors['grey'])
#plotting the content for the graph

plot_vol.plot(volume_plot, color='darkgrey', linewidth=2, label='Volume')
#plotting MACD chart

plot_MACD = axes[2]
# formatting the labelling to the right side of the graph and adding text

plot_MACD.yaxis.tick_right()
plot_MACD.set_ylabel('MACD', fontsize=14)
plot_MACD.yaxis.set_label_position("right")
plot_MACD.yaxis.label.set_color(colors['white'])
plot_MACD.grid(axis='y', color='gainsboro', linestyle='-', linewidth=0.5)
plot_MACD.set_axisbelow(False)

#formatting the box layout by removing the top and left side

plot_MACD.spines['top'].set_visible(False)
plot_MACD.spines['left'].set_visible(False)
plot_MACD.spines['left'].set_color(colors['grey'])
plot_MACD.spines['bottom'].set_color(colors['grey'])

#plotting the MACD line
plot_MACD.plot(macd, 'g')
plot_MACD.plot(exp3, 'r')
