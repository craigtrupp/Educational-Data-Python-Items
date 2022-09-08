#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:55:49 2022

@author: craigrupp
"""

# =============================================================================
# Lambda!
# Sometimes we need to put some conditions to the indices. 
# In such cases, you need to use a lambda function inside iloc[].
# =============================================================================

# =============================================================================
# Let's figure out what we can do using lambda:
# 
# data.iloc[lambda x: x.index < 5]
# This code will output the first five rows of the dataset, the rows with indices 0, 1, 2, 3, 4.
# 
# lambda x- x is the argument we will work with (item of the data set);
# x.index - extract only values of indices of rows;
# x.index < 5 - the condition according to which we will extract data. Here, only rows with less than 5 indices.
# =============================================================================

import pandas as pd

# Read csv file
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv')
data.head(1)
data.index
data.info()
# Extract data with even indices using iloc and modulus to check for remainder
even = data.iloc[lambda x: x.index % 2 == 0, :]
# Extract data with odd indices
odd = data.iloc[lambda o: o.index % 2 != 0, :]

# Output data
print(even.head(), '\n\n', odd.tail(), '\n', data.shape[0], even.shape[0], odd.shape[0])

#iloc multiple formatting, all columns returned if column argument not set
even.iloc[2]
even.iloc[2, :2]
even.iloc[2, :]


# =============================================================================
# You are already familiar with the .loc[] function, but here we will expand its possibilities.
# 
# One of the most useful tools is to set conditions on a column to extract specific values. 
# 
# So, you just put the condition of the column inside .loc[] function. Look at the several conditions and outputs.
# =============================================================================

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col=0)
data.head(2)
# Extract all rows from the column 'name' and 'hazardous'
data_extracted = data.loc[:, ['name', 'hazardous']]
data_extracted.head(2)
data_extracted['hazardous'].value_counts()
# Filter data:  extract columns where 'hazardous' is True.
data_filtered = data_extracted.loc[data_extracted['hazardous'] == True]

# Output data set
print(data_filtered.head())
data_filtered['hazardous'].value_counts()


# =============================================================================
# Deal w/Multiple Conditions
# & or | operators along with each condition within in it's own ()
# &	- It is used when we want to make the first and the second conditions satisfied.
# | = It is used when we want a condition to be satisfied
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col = 0)
data_extracted = data.loc[(data['est_diameter_min'] > 3.5) & (data['hazardous'] == True)]
print(data_extracted)
# Subset
data_extracted[['name', 'absolute_magnitude', 'hazardous']].head(5)


# =============================================================================
# Suggested Formatting for Readability
# Common to put conidition in it's own variable before passing to loc
# =============================================================================
# =============================================================================
# Write the first condition: values from the column'est_diameter_min' are less than 0.01. Assign it to the variable condition_1.
# Write the second condition: values from the column 'absolute_magnitude' are greater than 20. Assign it to the variable condition_2.
# Write the third condition: values from the column 'hazardous' are equal to False. Assign it to the variable condition_3.
# Write the general condition the satisfy requirement: (condition_1 and condition_2) or condition_3.
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col = 0)
condition_1 = data['est_diameter_min'] < 0.01
condition_2 = data['absolute_magnitude'] > 20
condition_3 = data['hazardous'] == False
# Write the general condition
data_extracted = data.loc[(condition_1 & condition_2) | condition_3]
print(data_extracted.head())



# =============================================================================
# Extract Data
# use the .isin() method 
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)
models = ['HONDA', 'FORD', 'MERCEDES-BENZ', 'HYUNDAI']
print(data.columns)
data_extracted = data.loc[data['Manufacturer'].isin(models)]
print(data_extracted['Manufacturer'].value_counts())



# =============================================================================
# Between Function
# This function titled .between(left_bound, right_bound). 
# You can apply it to numerical columns specifying numbers' left and right bounds. 
# Look at the example and learn how we can combine .between() and .loc[] statements.
# 
# Inclusive Argument for either left boundary or right boundary default is true for each
# .between(2, 3, inclusive = 'right') - extract data where 'Engine_volume' > 2 and 'Engine_volume' <= 3
# .between(2, 3, inclusive = 'left) - extract data where 'Engine_volume' >= 2 and 'Engine_volume' < 3
# .between(2, 3, inclusive = 'neither') - extract data where 'Engine_volume' > 2 and 'Engine_volume' < 3
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)

fuel_types = ['Plug-in Hybrid', 'Hybrid']
# Put the condition on the column 'Price'
condition_1 = data['Price'].between(15000, 20000, inclusive = 'left')
# Put the condition on the column 'Year'
condition_2 = data['Year'].between(2015, 2020, inclusive = 'neither')
# Put the condition on the column 'Fuel_type'
condition_3 = data['Fuel_type'].isin(fuel_types)

# Unite three conditions
data_extracted = data.loc[condition_1 & condition_2 & condition_3]

print(data_extracted.head())



# =============================================================================
# Find the Smallest and Largest Values of a particular column
# If you want to sort by one column and then by another, just put a list with column names in needed order
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)
data_smallest = data.nsmallest(15, 'Year')
print(data_smallest['Year'].head(15))

# Similar to a secondary groupby type column in a SQL query
data_smallest = data.nsmallest(5, ['Year', 'Engine_volume'])
print(data_smallest[['Year', 'Engine_volume']].head())

# Using keep argument w/All
data_smallest = data.nsmallest(6, 'Year',
                             keep = 'all')
print(data_smallest['Year'], data_smallest.shape[0])
# Note how the 6th Year is a new value (1953), the keep argument then extends the amount of returned matches to include all found records with that year


# Default
# Case without using keep = 'all' argument
data_smallest = data.nsmallest(6, 'Year')
print(data_smallest['Year'], data_smallest.shape[0])
# Note how just the one instance of 1953 is collected here unlike the previous call w/nsmallest

#Largest
data_largest = data.nlargest(5, 'Year')
print(data_largest[['Year', 'Manufacturer', 'Model']])

# Keep all from largest year
data_largest_keep = data.nlargest(4, 'Year', keep='all')
print(data_largest_keep, data_largest_keep[['Year', 'Manufacturer', 'Model']].head(10))
# 47 total rows, here's just a subset of 10 all showing the nlargest year 



# =============================================================================
# Corr Function : Relationship 
# 1 means that two values depend on each other directly proportional (if one value increases, another increases too).
# -1 means that two values depend on each other inversely proportional (if one value increases, another decreases).
# 0 means that the two values that depend aren't proportional.
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)

# Apply .corr() function
print(data.corr())


