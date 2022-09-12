#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:27:51 2022

@author: craigrupp
"""
# Type Conversion
# =============================================================================
# You can discover that data can be stored in the dataset in the wrong format or type. The most common cases are:
# 
# storing integer or float values as string variables.
# storing date and time values as strings.
# storing values in a form that can be converted to a more suitable one.
# =============================================================================

import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/exercise.csv', index_col = 0)
data.head(2)
data.info()
# Time is a string/object type column that has the numerical minutes we want to extract
data['time'] = data['time'].apply(lambda x: int(x[:-4]))
print(data.sample(10))
data.info()


# Data Binning
# =============================================================================
# Sometimes it makes sense to bin the data into multiple buckets: to divide it into classes, for histogram building, etc. Data binning is applied to the continuous numerical data.
# 
# We won't dive deep into it and just explore two functions: cut and qcut:
# 
# cut: divides the data into predefined bins, usually equal-sized.
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/titanic.csv')
print(data.head(2))

def totalPercent(x):
    return f"{str(round((len(x)/len(data)) * 100,2))}% was returned for age bin : {x.name}";


data_copy = data.copy()
data_copy['age_bin'] = pd.cut(data_copy['Age'], bins=4)
print(data_copy[['Age', 'age_bin']].head(10))
# create 4 equal-sized bins
cut_data = pd.cut(data['Age'], bins = 4)
print(cut_data, type(cut_data), '\n', cut_data.unique(), len(cut_data.unique()))
# set defined bins
cut_data = pd.cut(data['Age'], bins = [20, 40, 60])
data_copy['age_set_bins'] = pd.cut(data_copy['Age'], bins=[20,40,60])
print(data_copy[['Age', 'age_bin', 'age_set_bins']].head(10))
print(data_copy.groupby('age_set_bins')['PassengerId'].agg('count'))
print(data_copy.groupby('age_bin')['PassengerId'].agg({'count'}))
print(data_copy.groupby('age_bin')['PassengerId'].apply(lambda x: print(x, type(x), len(x))))
print(data_copy.groupby('age_bin')['PassengerId'].apply(lambda y: print(totalPercent(y))))

#qcut, or quantile-based cut, divides data into equal-sized categories: each interval contains equal number of entries.

# create 4 bins
qcut_data = pd.qcut(data['Age'], q = 4)
print(qcut_data)
# set defined quantiles
qcut_data = pd.qcut(data['Age'], q = [0, 1/3, 2/3, 1])
print(qcut_data)




