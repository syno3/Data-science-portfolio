# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

'''
- OPENED AND PARSED THE CSV FILE
- REMOVED WEIRD TABLES
- TRIED TO CHANGE INT TABLES FROM STRINGS
- CREATED A NEW VARIABLE WITH SIMILAR CONTENT AS DROPPED INT
- REPLACED NAN VALUES WITH O 
---- PIE CHART -----
- CREATE PIE CHART FROM SERIES COUNTED

'''
wearables_data =  pd.read_csv('Wearables.csv')
dropped = wearables_data.drop(columns=['Duplicates.note.1', 'Image'])
dropped_int = dropped.apply(pd.to_numeric, errors='ignore')
dropped_int_fill = dropped_int
dropped_int_fill["Price"] = dropped_int["Price"].fillna(0)

def visualization_piechart(data):
    #create pie chart from series counted
    ax = data.value_counts().plot(kind='pie', figsize=(5, 5),fontsize=10,autopct='%1.1f%%',shadow=True)
    ax.set_title("Distribution of Most Popualar Categories")
    
''' run the code to get the various names,
due to lack of data cannot use other methods

'''
#print(dropped_int_fill.loc[0])
visualization_piechart(dropped_int_fill["Company...Country"])
#print(dropped_int_fill.loc[0])