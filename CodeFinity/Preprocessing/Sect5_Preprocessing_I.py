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


# Replace with Interpolation
# =============================================================================
# Another approach to deal with numerical data is using interpolation. 
# Each NaN value will be replaced with the result of interpolation between the previous and the next entry over the column.
#  Let's apply the interpolate() function to numeric column Age by setting the limit direction to forward. T
#  his means that linear interpolation is applied from the first line to the last.
# =============================================================================
data_two = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/titanic.csv')

data_na_age = data_two.loc[data_two['Age'].isna()]
data_nonna_age = data_two.loc[~data_two['Age'].isna()]
data_two['Age'].isna().sum()
print(f"Total Null age values from loc condition : {data_na_age.shape[0]}. Directly from the imported flat file : {data_two['Age'].isna().sum()}")
print('Ages before the interpolation:', data_two['Age'].tail(5))

data_two['Age'] = data_two['Age'].interpolate(method='linear', limit_direction = 'forward')
print('Ages after the interpolation:', data_two['Age'].tail(5))

# Let's look at a few more interpolated values from the old dataframe against the new interpolated Age values that replaced null values
# See how row 5 is data_two has been generated by values in Age at row 4 & 6 following that dataframe having it's column interpolated
print(data_nonna_age['Age'].head(20))
print(data_two['Age'].head(20))


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

# Tilde usage to inversely grab rows from dataframe not in defined mean/std outlier range 
combined_outliers = data[age_mean_std_over|age_mean_std_under]
within_range = data[~(data.index.isin(combined_outliers.index))]
combined_outliers['Age'].describe()
within_range['Age'].describe()

plt.hist(combined_outliers['Age'])
plt.hist(within_range['Age'])

# ============================================================================= 
# Removing Outliers Using IQR
# The following code removes all data outside the range [q25 - 1.5*IQR; q75 + 1.5*IQR]:
# Leave the values that fit the interval [q25 - 1.5*IQR; q75 + 1.5*IQR], where IQR = q75 - q25. IQR is Inter Quartile Range
# =============================================================================

# Take quantile percntages of ages column
q25, q50, q75 = data['Age'].quantile(q=[0.25, 0.5, 0.75])
print(q25, q50, q75)
iqr_age_frame = data.loc[data['Age']]
# List of ages in IQR
list(range(int(q25),int(q75+1)))
iqr = 1.5 * (q75-q25)
iqr
# Bool Outlier Series
age_inclusive_iqr = data['Age'].between((q25 - iqr), (q75 + iqr), inclusive='both')
# Frames
inclusive_iqr_frame = data.loc[age_inclusive_iqr]
inclusive_iqr_frame['Age'].describe()
non_inclusive_iqr_frame = data.loc[~age_inclusive_iqr]
non_inclusive_iqr_frame['Age'].describe()

# IQR Equation Outliers Excluded on Age Values percentage
print('Removed Data : ', round((1-(len(inclusive_iqr_frame)/len(data)))*100, 2), '%')


# Using Fare Data to Visualize Outliers (Run in Block)
fare_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/10db3746-c8ff-4c55-9ac3-4affa0b65c16/titanic.csv')

q25, q50, q75 = fare_data['Fare'].quantile(q=[0.25, 0.5, 0.75])
iqr = q75 - q25
# Store the data without outliers in fare variable
fare = fare_data['Fare'].loc[(fare_data['Fare'] > q25 - 1.5*iqr) & (fare_data['Fare'] < q75 + 1.5*iqr)]
# Fare data frame is not holding the second row (index 1 value in the original dataframe)
print(fare.loc[0:6])
print(fare_data['Fare'].loc[0:6])
# Run below to see the quantiles, iqr and outlier range check 
q25, q75, iqr, q25 - (1.5 * iqr), q75 + (1.5 * iqr)
bins = range(0, 90, 10)
plt.hist(fare_data['Fare'], bins=bins, color='orange')
# Outliers above, non outliers below
plt.hist(fare, bins=bins)







