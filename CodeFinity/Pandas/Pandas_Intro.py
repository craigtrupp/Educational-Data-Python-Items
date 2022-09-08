#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 08:16:12 2022

@author: craigrupp
"""
import pandas as pd
data_1 = [2, 4, 8, 16]
data_2  = ['New York', 'California', 'Chicago', 'Alaska']
# Write your code here
series_1 = pd.Series(data_1)
series_2 = pd.Series(data_2)

print(series_1 , series_2)


dataset = {'name' : ['Ann', 'Alex', 'Kevin', 'Kate'], 
          'age' : [35, 12, 24, 45]}

data_frame = pd.DataFrame(dataset)
print(data_frame)

dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pd.DataFrame(dataset)

# Adding a new column
countries['population'] = [61399000, 75967000, 39244, 380200, 10380491, 5496000, 2424200]
print(countries)


# =============================================================================
# Sometimes, some columns do not carry any information, and it is better to delete them. To do this, pandas has the drop() function. Let's look at the syntax of this function.
# 
# drop(index, columns, axis). Here
# 
# index - the indexes of the rows which we want to delete, it is used when axis=0.
# columns - the name of the columns, which we want to delete, (it is used when axis=1).
# In this section we will work with the next data frame.
# 
# axis - choose whether to remove labels from the rows(0) or columns(1), (default is 0).
# Let's look at it.
# =============================================================================
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : [None, None, 'Europe', None, 'Europe', None, 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}

countries = pd.DataFrame(dataset)
countries_in_place = pd.DataFrame(dataset)
print(countries)
print(countries_in_place)

#Deleting A Column, Re-Assign, Inplace
countries = countries.drop(columns='continent', axis=1)
print(countries)
countries_in_place.drop(columns='continent', inplace=True)
print(countries_in_place)


# Work with Column(s) - Type Returns
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pd.DataFrame(dataset)
# Printing capital column
capitals = countries['capital']
print(capitals, type(capitals))

# Multiple Columns - Type
countries[['country', 'capital']]
type(countries[['country', 'capital']])




# =============================================================================
# We can also access data by index in the data frame. Accessing rows by index is possible in several ways:
# 
# .iloc - used to access by numeric value (starting from 0).
# .loc - used to access by string label.
# =============================================================================
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pd.DataFrame(dataset)
print(countries)

# Accessing the third row (Zero Indexing as per)
print(countries.iloc[2])
# Accessing the seventh row
print(countries.iloc[6])
# Accessing slice of rows, & columns
print(countries.iloc[:2, :2])
# Accessing specifc rows & columns
print(countries.iloc[[0, 2], [0,2]])



# Accessing Labels (set_index to non numeric field for common operation of indexing a column)
country_index = countries.set_index('country')
print(country_index.head(1))
print(country_index.index, '\n', country_index.columns)

#Accessing Specific row/column
print(country_index.loc['Thailand', 'capital'])
# Multiple columns
print(country_index.loc['Thailand', ['capital', 'continent']])
# Slice, all columns (inclusive unlike iloc which sets exclusive boundary)
print(country_index.loc['Thailand':'Monaco', :])
# All rows, select column(s)
print(country_index.loc[:, 'capital'])


# Column / DataFrame Length properties (shape property) 
print(f"Overall count for rows/columns in dataframe : {country_index.shape}", type(country_index.shape))
# Tuple return, access indices just like a list/array
print(f"Total Rows : {country_index.shape[0]}")
print(f"Total columns : {country_index.shape[1]}")
print(f"Length of column values : {len(country_index['capital'])} : same as the rows what ya know")





