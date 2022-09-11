#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 10:19:58 2022

@author: craigrupp
"""

# =============================================================================
# As you already know, it is possible that raw data can contain some dirty data. It can be:
# 
# NaN: undefined or missing data.
# empty strings.
# infinite: very large data.
# incorrect data: for example, 'Female' in the Price column, that contains numeric data (this value could be stored into the wrong cell accidentally). You may find impossible values of the user's age, for example, if this value should be entered by him manually (like -1, 110, 0, etc.).
# outliers: critically small or big values(for example, 250 cm in the Height column, or 112 yrs in the Age column), usually in a small amount. They may affect your result of analysis or model weights, so sometimes it makes sense to remove them.
# Let's learn how to 'clean' your data and not to lose some useful info.
# =============================================================================



import pandas as pd
import numpy as np

# Work w/NANs
# Chaining .sum on .isna() will return the count off all null values in a column
 
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/titanic.csv')
print(data.head(2))
print(data.isna().sum())


# =============================================================================
# Drop NaNs
# The easiest way to deal with missing data is just to drop the records that contain it. Use the method dropna(). 
# Note that it doesn't change the current dataframe, but returns the new one. 
# To change the current dataframe, add parameter inplace assigned with True:
# =============================================================================
clean_data = data.dropna() # data is not modified, but clean_data now contains no NaNs
# data.dropna(inplace=True) # data is modified
print(clean_data.isna().sum())



# Replace Numerical Missing Data with Values Or Other
# =============================================================================
# The popular approaches to deal with NaNs for numerical data are:
# 
# replace with the mean value: good for the normal data distribution and when the number of NaNs is small.
# replace with the mode value: good for exponential distributions and a small amount of NaNs.
# replace with the max or min value: good if you are sure there are no outliers that may affect the result.
# replace with some const value: for example, 0 or 1, if the possible value is either 0 o

# To replace the NaNs, you can use fillna():
# data.fillna(some_val) # replaces NaN with some_val
# or
# data.fillna(some_val, inplace=True) # change the data in-place

# Also, you can use replace(old_val, new_val) to replace not only NaNs, but any other values:

# =============================================================================

data['Age'].isna().sum()
data['Age'].value_counts(ascending=False)
# Let's look at median and mean age to see what might be most appropriate, from the value counts above Earlys 20s and Late Teens has high value_counts
print(data.agg({'Age': [np.mean, np.median, 'mean', 'max', 'min', 'std', 'var']}))
print(data['Age'].mean(), '\n', data['Age'].mode(), '\n', data['Age'].median())

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Age'].isna().sum()

# Display Histogram of Age distribution
import matplotlib.pyplot as plt

plt.hist(data['Age'])
plt.title('Titanic Age Distribution : Post Null Value Fill')
plt.xlabel('Age')
plt.ylabel('Count Per Age Bin')
plt.show()


# =============================================================================
# Replace Categorical Missing Data with Values
# To deal with categorical data:
# 
# replace with some constant or the most popular value
# create a new category for these values.
# process the data after converting it to the numerical. We'll use this approach later.
# Let's explore for each column Cabin and Embarked(these columns contain NaNs) and figure out how to proceed with the NaNs.
# =============================================================================
data['Embarked'].isna().sum()
data['Embarked'].value_counts(ascending=False)
# Drop in place with only 2 values
data.dropna(subset='Embarked',inplace=True)
total_emb_null = data['Embarked'].isna().sum()

percent_null_cabin = round((100 * data['Cabin'].isna().sum() / len(data['Cabin'])), 2)
total_cab_null = data['Cabin'].isna().sum()
len(data['Cabin']), data['Cabin'].shape
f"The total null count of {total_cab_null} as a percentage against all Embarked known values, {len(data['Embarked'])} is {percent_null_cabin}%"


