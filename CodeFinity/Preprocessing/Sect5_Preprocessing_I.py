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

# Unique categorical values and # of unique values
print(data['Cabin'].unique(), data['Cabin'].nunique())
# choose any other value except already presented in the Cabin column and replace all NaNs with it. (For example, it can be 'Z' or 'X').
data['Cabin'].replace(np.nan, 'Z', inplace=True)
data['Cabin'].isna().sum()

# =============================================================================
#  Check for any duplicates
#  method drop_duplicates
#  Method will return the dataframe with any duplicates removed, use inplace if wanting to change existing variable
# =============================================================================
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
print(len(df), len(df.drop_duplicates()), f"Total duplicate rows : {len(df) - len(df.drop_duplicates())}")
df.drop_duplicates(inplace=True)
len(df)


# Check titanic (or any dataframe), with your own function!
def checkDFrameDuplicates(frame):
    """
    Parameters
    ----------
    frame : Dataframe.

    Returns
    -------
    Total found duplicate rows in dataframe.
    """
    dframe_total_rows = len(frame)
    found_duplicate_rows = dframe_total_rows - len(frame.drop_duplicates())
    return f"Found duplicate rows : {found_duplicate_rows}" if found_duplicate_rows > 0 else "No duplicate rows!"
    
print(checkDFrameDuplicates(df)) 
print(checkDFrameDuplicates(data))    



# =============================================================================
# Removing Outliers
# Outliers are some extra values that do not fit the defined interval. 
# These values can affect some metrics(like mean, mode, etc.) or model weights. 
# 
# There are some popular ways to define the allowable interval (limits of acceptable value for some distribution):
# 
# remove all the values that form the first and the last 1% of values (presented in ascending order).
# Leave the values that fit the interval [q25 - 1.5*IQR; q75 + 1.5*IQR], where IQR = q75 - q25. IQR is Inter Quartile Range. Remove other values.
# leave all data that fits the interval [mean - std; mean + std]. Remove other values.    
# =============================================================================

#Let's find all the data outside the range [mean - std; mean + std] and check how much is outside 
age_central_stats = data.agg({'Age': ['min', 'max', 'mean', 'std', 'var']})
age_central_stats.loc[age_central_stats.index == 'mean']
age_mean, age_std = round(data['Age'].mean(), 0), round(data['Age'].std(), 0)

age_mean_std_over = data['Age'] > (age_mean + age_std)
age_mean_std_under = data['Age'] < (age_mean - age_std)
print(age_mean_std_over.nunique())
print(age_mean_std_under.unique())
# Boolean index subsetting
combined_outliers = data[age_mean_std_over|age_mean_std_under]
within_range = data[~(data.index.isin(combined_outliers.index))]
len(within_range)
within_range.shape[0] + combined_outliers.shape[0]


len(combined_outliers), len(within_range), len(data)
combined_outliers['Age'].head(10)
combined_outliers['Age'].value_counts(ascending=False)




