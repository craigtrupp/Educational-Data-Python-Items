#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:02:34 2022

@author: craigrupp
"""

# Label Encoding
# =============================================================================
# Label Encoding is a process of encoding non-numerical values into numerical categories. 
# Therefore, Label Encoding refers to converting the values into numeric forms and later converting them into machine-readable forms. 
# Machine Learning algorithms decide how to operate those labels. 
# It is a significant preprocessing step for structured datasets in supervised learning.
# 
# Before the Encoding, inspect the data you are working with.
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/titanic.csv')

# Let's get an idea of our non null values
data_cabin_nonnull = data[~data['Cabin'].isna()]
data_cabin_nonnull['Cabin'].head(25)

# Ahhh we see that some rows have what appears multiple cabins. Let's get the counts of passengers with more than 1 cabin
cabin_counts = data['Cabin'].apply(lambda x: 0 if pd.isna(x) else len(x.split(" ")))
cabin_counts.value_counts()

def cabinLabel(x):
    return 'Z' if pd.isna(x) else x[:1]

def cabinCount(x):
    return x.count(' ') + 1

data_cabin_nonnull.reset_index(inplace=True)
data_cabin_nonnull['Cabin'].head(25)
data_cabin_nonnull['Cabin'].iloc[[7, 19, 22]]
data_cabin_nonnull['Cabin'].iloc[[7, 19, 22]].apply(lambda x: 'Z' if pd.isna(x) else x[:1])
data_cabin_nonnull['Cabin'].iloc[[7, 19, 22]].apply(lambda y: y.count(' '))
"C23 C25 C27".split(" ")


data['CabinCount'] = 0
data[['Cabin', 'CabinCount']].head(10)
data['CabinCount'] = data['Cabin'].apply(lambda x: 1 if pd.isna(x) else x.count(' ') + 1)
data['Cabin'] = data['Cabin'].apply(lambda y: 'Z' if pd.isna(y) else y[:1])
# Multi Cabin Units
data[['Cabin', 'CabinCount']].loc[data['CabinCount'] > 1]

# Sum of Total Counts by Cabin Letter Assigned to Passenger Cabin w/quick bar chart to look at the Series
cabin_total_counts = data.groupby('Cabin')['CabinCount'].agg('sum').sort_values(ascending=False)
type(cabin_total_counts)
cabin_total_counts.hist()
plt.bar(cabin_total_counts.index, cabin_total_counts.values)


# Label Mapping 
# =============================================================================
# String values cannot be recognized by ML model, so the idea is to create some mapping and change these values into numerical. 
# We can do it manually by creating a mapping and transforming the column data:
# 
# =============================================================================
# Apply the Label Encoding to the Embarked column by creating a mapping. Modify this data in-place.
# Column values are currently a string/object and will need to be a numeric identifier to be ML recognizable
data['Embarked'].unique()

# Get all unique column values and create a range to iterate through after getting the length of the unique() return
# Pass iterabled to mapping's key value so the unique keys will be assigned a numeric value to map
mapping = {data['Embarked'].unique()[i]: i for i in range(len(data['Embarked'].unique()))}
mapping
data['Embarked'][:5]
[mapping[val] for val in data['Embarked'][:5]]
data['Embarked_Numeric'] = [mapping[val] for val in data['Embarked']]
data[['Embarked', 'Embarked_Numeric']].head(25)
