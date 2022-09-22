#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:33:06 2022

@author: craigrupp
"""
# Countplot
# =============================================================================
# A countplot is a plot that takes a categorical list and returns columns that represent the number of list entries for each category.

# To initialize a countplot, we need to input at least 1 parameter: x - the column in which values will be counted.
# We may also use y instead of x to change the orientation of the plot.
# =============================================================================
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

guests_list = ['Girl', 'Boy', 'Boy', 'Boy', 'Girl', 'Boy', 'Boy', 'Boy', 'Girl', 'Boy', 'Girl', 'Girl', 'Girl', 'Girl', 'Girl', 'Girl']

sns.countplot(x=guests_list)
plt.show()

# With Pandas
# =============================================================================
# To create a countplot based on a DataFrame:
# 
# To initialize a countplot based on the pandas DataFrame we need to input at least 2 parameters: x - the column whose values will be counted, and data - the DataFrame containing the data.
# 
# You can change x to y to change the orientation of the plot.
# =============================================================================
data_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/bamboo.csv')

print(data_df.head())
print(data_df.columns)

ax = sns.countplot(x='Bamboo', data=data_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Scatterplot
# =============================================================================
# A scatterplot uses dots to represent values for two different numeric variables. 
# The position of each dot on the horizontal and vertical axis indicates values for an individual data point
# To initialize a scatterplot based on the pandas DataFrame we need to input at least 3 parameters: 
# x, y - columns-coordinates for the plot and data - the DataFrame containing the data.
# =============================================================================

# New Data
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/ice_chill.csv')
print(df.head())

sns.scatterplot(x='x', y='y', data=df)

plt.show()


# 3-Variable Scatterplot - Hue
# =============================================================================
# To create a 3-variable scatterplot based on a DataFrame:
# 
# To initialize a 3-variable scatterplot based on the pandas DataFrame we need to input at least 4 parameters: 
# x, y - columns-coordinates for the plot, hue - column for the third variable, and data - the DataFrame containing the data.
# =============================================================================

# More Data
df_2 = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/bilibili.csv')
# Notice More categorical data like gender/daytime columns
print(df_2.head())
print(df_2.columns)


# Evaluate if daytime column impacts relationship between bill/tips

sns.scatterplot(x='bill', y='tips', data=df_2, hue='daytime')

plt.show()


# Color Setting
# =============================================================================
# Set Colors for Hue Variable
# Palette to map unique values to particular color desired
# =============================================================================
hue_unique_values = df_2['daytime'].unique()
hue_nuniqe_values = df_2['daytime'].nunique()
print([hue_unique_values, hue_nuniqe_values])

# Key represents column, value represents color palette to pass to scatterplot function
hue_mapping = {'breakfast': 'blue', 'lunch':'purple', 'dinner':'green'}

# Build Scatter, define palette_mapping
sns.scatterplot(x='bill', y='tips', hue='daytime', palette=hue_mapping, data=df_2)

plt.show()


# Lineplot
# =============================================================================
# To create a lineplot based on a DataFrame:
# 
# To initialize a lineplot based on the pandas DataFrame we need to input at least 3 parameters:
# x y - columns-coordinates for the plot and data - the DataFrame containing the data.
# =============================================================================


# New Data
line_data_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/hungry.csv')
print(line_data_df.head())

sns.lineplot(x='time', y='level', data=line_data_df)

plt.xticks(rotation=45)

plt.show()


# 3 Variable Lineplot ... hue again!
# =============================================================================
# To create a 3-variable lineplot based on a DataFrame:
# 
# To initialize a lineplot based on the pandas DataFrame you need to input at least 4 parameters:
# x y - columns-markers for the plot, hue - the third variable and data - the DataFrame containing the data.
# =============================================================================
line_hue = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/lineplothue.csv')
print(line_hue.head())

sns.lineplot(x='year', y='population', hue='season', data=line_hue)

plt.xticks(rotation=45)

plt.show()


# Histplot
# =============================================================================
# A histogram (aka histplot) is a classic visualization tool that represents the distribution 
# of one or more variables by counting the number of observations that fall within discrete bins.
# 
# To create a histplot based on a DataFrame:

# To initialize a histplot based on the pandas DataFrame we need to input at least 2 parameters: 
# x/y - the column which values will be used to create a histplot, and data - the DataFrame containing the data.
# =============================================================================
hist_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/fish.csv')
print(hist_df.head())

# More common x-axis oriented for target variable with frequency/count on y-axis
sns.histplot(x='answer', data=hist_df, binwidth=0.15, bins=10)
plt.show()

# y-based : harder to read visualize
sns.histplot(y='answer', data=hist_df, binwidth=0.2)
plt.show()

























