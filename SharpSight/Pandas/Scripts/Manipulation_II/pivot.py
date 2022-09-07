##################################################
# PIVOT
#
# You'll learn:
# 
# - How to use the .pivot() method
# - How to reshape your data from long to wide
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
##################################################



#----------------
# IMPORT PACKAGES
#----------------
import pandas as pd
import numpy as np



#------------
# CREATE DATA
#------------

revenue_tidy = pd.DataFrame({'region':['Europe', 'Europe', 'North America', 'North America']
                            ,'quarter':['Q1','Q2','Q1','Q2']
                            ,'revenue':[65000,62000,60000,63000]
                            })



print(revenue_tidy)
#          region quarter  revenue
#0         Europe      Q1    65000
#1         Europe      Q2    62000
#2  North America      Q1    60000
#3  North America      Q2    63000

revenue_tidy.pivot(index=['region'], columns=['quarter'], values='revenue')
revenue_pivot = revenue_tidy.pivot('region', 'quarter', 'revenue')
print(revenue_tidy, '\n\n', revenue_pivot)
print(revenue_pivot.index, revenue_pivot.columns)
print(revenue_tidy.pivot_table(values='revenue', index='region', columns=('quarter')).agg(['mean', 'max']))
revenue_pivot_table = pd.pivot_table(revenue_tidy, )
#-----------------------
# PIVOT
# - reshape long to wide
#-----------------------

revenue_tidy.pivot(index = 'region'
                   ,columns = 'quarter'
                   ,values = 'revenue'
                   )




df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df
# Call below is for agg func when categorical type rows have differing values 
# pandas takes the frame, values argument detail which values you'd like to put for each unique column value delcared
# Index sets the structure of how you'd like to declare your groupings (see type hierarchical output)
# Columns take the unique values for the C and spreads that over columns (values of 'large' and 'small' in column C) are moved into their own column
# 
print(pd.pivot_table(df, values=['D','E'], index=['A', 'B'], columns=['C']))
pd.pivot_table(df, values='E', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
df[['A', 'B', 'C']].value_counts()
#EOF