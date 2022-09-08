#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 08:57:57 2022

@author: craigrupp
"""

# =============================================================================
# Read in Data (Common CSV Pandas initial import)
# =============================================================================
import pandas as pd

# Set First Column as Index (Common if Initial Column is Index from file)
data_frame = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')
data_frame_idx = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv', index_col=0)
print(data_frame.head(1))
print(data_frame_idx.head(1))

# =============================================================================
# Viewing the Data / Information about the Data - head, tail, sample

# To view the first few rows of a dataset, we can use the head() function. 
# This function takes an integer as its only argument (it defaults to 5)
# To view the last few rows of a data frame, we can use the tail() function, which follows the same structure
# sample() - this function returns random records from a data frame (same structure)

# There is a very useful method in pandas that gives us basic information about a dataset and the method is called info()
# See all Column Names as a list
# We can also get a summary of all types of data that are in your data frame. For this we have to use the following method: dtypes. 
# =============================================================================
print(data_frame_idx.head())
print(data_frame_idx.tail(2))
print(data_frame_idx.sample(3))
print(data_frame_idx.info())
# Note Index from slightly different columns property return can be accessed just like any list
print(data_frame_idx.columns, [x for x in data_frame_idx.columns], data_frame_idx.columns[0])
# Same Detail available from info as well, Series type return that can be indexed similar to an .iloc (without columns as Series only)
print(data_frame_idx.dtypes, type(data_frame_idx.dtypes), '\n\n', data_frame_idx.dtypes[:2])


# =============================================================================
# Finding Null Values
# Often data frames have missing values (exactly None, np.NaN). 
# And when we work with data frames, we need to be able to detect this missing data. 
# To do this, pandas has special functions.

# The first function is isna(). 
# This function returns a boolean data frame. 
# Accordingly, True value means missed value in the data frame, and False value means not missed value

# The second function is isnull(). 
# This function performs the same as the previous one. There is no difference between them
# =============================================================================
import numpy as np

dataset = {'animal': [np.NaN, 'Dog', np.NaN, 'Cat','Parrot', None],
'name': ['Dolly', None, 'Erin', 'Kelly', None, 'Odie']}
animal = pd.DataFrame(dataset)
# Find missing values
missing_value = animal.isna()
print(missing_value)
# Second function
animal.isnull()


# =============================================================================
# Dropping Null Values
# If our data contains null values in certain columns, we need to delete these rows. 
# In pandas, it can be done with the dropna() function.
# This will default to delete any row with a null value in one of its' columns (axis=0)
# =============================================================================
data_frame = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine_with_nan.csv', index_col=0)
# Inspect DataFrame, Check null values & chain sum across columns, confirm with .info
data_frame.head(1)
data_frame.isna()
data_frame.isna().sum()
data_frame.info()
# Write your code here, two ways to approach (inplace .. is permanent so be careful!)
data_frame_without_missing_values = data_frame.dropna()
data_frame_without_missing_values.info()
data_frame.dropna(inplace=True)
data_frame.info()


# =============================================================================
# Filling Null Values
# To account for NaN values but preserve every row of the data frame, we can use the fillna() function to fill each empty cell 
# A value needs to be placed here and can commonly be used as a function to fill mean type values for numerical column types
# =============================================================================
null_values = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine_with_nan.csv', index_col=0)
# Note null values remain
null_values.info()
# No longer!
null_values.fillna(0, inplace=True)
null_values.info()



# =============================================================================
# Describing the Data : Dataframe & Columns
# mean, mode, max, min usage
# =============================================================================
des_frame = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv', index_col=0) 
des_frame.head(1)
# Add String type to show usage on dtypes
des_frame['Wine_Type'] = ['White' if a % 2 == 0 else 'Red' for a in range(456)]
des_frame.info()

# Mean Across Numerical DTypes, Note how created string Dtype.object is not included in calculation across dataframe
des_frame.mean()
des_frame.mode()
des_frame.value_counts(ascending=False)
# Select only valid columns before calling the reduction.
# FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError
des_frame[['fixed acidity', 'citric acid']].mean()
des_frame[['fixed acidity', 'citric acid']].mode()

# Will include Object types from dataframe
des_frame.max()
des_frame.min()

des_frame['Wine_Type'].value_counts(ascending=False)

# =============================================================================
# Summary Statistics
# This function includes the following metrics from data:
# total number of lines, average or mean value, standard deviation, the smallest(min) and the largest(max) values in the dataset, 25th, 50th, and 75th percentiles.
# Note How Object type is ignored
# =============================================================================
des_frame.describe()
des_frame.columns


# =============================================================================
# Sum() & Count()
# count() - this function counts not null (not None, not np.NaN) cells for each column.
# sum() - this function returns the sum of the values for each column.
# =============================================================================
des_frame.count()
des_frame[['fixed acidity', 'residual sugar']].count()

# Note to test you must make a copy or changes to new variable will impact original 
des_frame_addnulls = des_frame.copy()
des_frame_addnulls.iloc[0:3, :] = np.nan
des_frame_addnulls.info()
des_frame_addnulls.count()
# Note how null values not counted
len(des_frame_addnulls)

# Sum adds up all strings
des_frame.sum()
# All but one column
des_frame.loc[:, des_frame.columns != 'Wine_Type'].sum()
# Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.
des_frame_addnulls.sum()
des_frame_addnulls.loc[:, des_frame_addnulls.columns != 'Wine_Type'].sum()
# Omit any String Columns
des_frame.loc[:, [x for x in des_frame.columns if des_frame[x].dtype != 'object']].sum()
des_frame.dtypes
des_frame['fixed acidity'].dtype


# =============================================================================
# Unique Values
# unique() call for dataframe
# =============================================================================
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}

countries = pd.DataFrame(dataset)
unique_countries = countries['country'].unique()
unique_continents = countries['continent'].unique()
print(unique_countries)
print(unique_continents)
# method only available to Series object / not a DataFrame
print(countries.unique())
print(countries['continent'].unique(), len(countries['country'].unique()))











