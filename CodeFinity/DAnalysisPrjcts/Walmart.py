#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:03:16 2022

@author: craigrupp
"""

# =============================================================================
# You have displayed this dataset at least 3 times, so you recognized that the column Date doesn't have 
# the format understandable for python (day, month, and year separated using ., but there should be - ). 
# Your task here is to follow the algorithm:
# 
# Convert column Date to datetime format.
# Print the first 5 rows of the column Date.
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/w-3', index_col=0)
print(df['Date'].dtype) # string object

df_copy = df.iloc[:5,:].copy()
print(df_copy.head(), '\n', df_copy.dtypes)
df_copy['Date'] = pd.to_datetime(df_copy['Date'], infer_datetime_format=True) # Provide format or specify infer_datetime_format=True for consistent parsing.
print(df_copy.head(), '\n', df_copy.dtypes)

# Convert column 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y') # Being more explicit when declaring removed user warning above when using the infer argument instead
print(df.dtypes)

# Print the first 5 rows of the column 'Date'
print(df['Date'].head())

# =============================================================================
# 0   2010-02-05
# 1   2010-02-12
# 2   2010-02-19
# 3   2010-02-26
# 4   2010-03-05
# Name: Date, dtype: datetime64[ns]
# =============================================================================


## Convert Temperature
# =============================================================================
# Convert column Temperature from Fahrenheit to Celsius, using the formula
# Rename column Temperature to Temp_Celsius
# Output the minimum of Temp_Celsius
# =============================================================================
# Convert 'Temperature' to Celsius
df['Temperature'] = (df['Temperature'] * (5/9)) - 32

# Rename the name of the column
df.rename(columns = { 'Temperature' : 'Temp_Celsius'} , inplace = True )

# Output the minimum of the column 'Temp_Celsius'
print(df['Temp_Celsius'].min()) # -27.855555555555554




## Deal with Incorrect Separator
# =============================================================================
# You know that to separate integer and fractional type points are used. 
# But you've already noticed that numbers here are separated by a comma; moreover, they don't relate to numerical data type.
# 
# Replace - by point . within the separator() function. 
# Convert data[column_name] to the floating-point data type.
# Apply function separator() to the column Weekly_Sales.
# Output the last five rows of the column Weekly_Sales.
# 
# =============================================================================
# Review Weekly Sales Column
print(df['Weekly_Sales'].head())

## Originaly type and output 
# =============================================================================
# 0     1643690-9
# 1    1641957-44
# 2    1611968-17
# 3    1409727-59
# 4    1554806-68
# Name: Weekly_Sales, dtype: object
# =============================================================================

# Define the function
def separator(data, column_name):
  data[column_name] = data[column_name].str.replace('-' , '.')
  data[column_name] = data[column_name].astype(float)


# Apply function to required column
separator(df, 'Weekly_Sales')

# Output the last five rows of the column `Weekly_Sales`
print(df['Weekly_Sales'].tail())

# =============================================================================
# 6430    713173.95
# 6431    733455.07
# 6432    734464.36
# 6433    718125.53
# 6434    760281.43
# Name: Weekly_Sales, dtype: float64
# =============================================================================



## Count Statistical Values

# Find the mean
mean = df['Temp_Celsius'].mean()
# Find the median
median = df['Temp_Celsius'].median()
# Find the mode
mode = df['Temp_Celsius'].mode()
# Find the standard deviation
std = df['Temp_Celsius'].std()
# Find the variance
variance = df['Temp_Celsius'].var()

print("The mean value is", mean)
print("The median is", median)
print("The mode is", mode)
print("The variance is", variance)
print("The standart deviation is", std)

# =============================================================================
# The mean value is 1.7772333368066466
# The median is 2.9250000000000007
# The mode is 0   -3.983333
# Name: Temp_Celsius, dtype: float64
# The variance is 104.25545192651256
# The standart deviation is 10.210555906830566
# =============================================================================

# Create Figure and Axes object
fig, ax = plt.subplots()
# Initialize the histogram for the 'Temp_Celsius' column
ax.hist(df["Temp_Celsius"])
# Title histogram as 'Temperature'
plt.title("Temperature Distribution")
plt.xlabel('Temperature in Celisus')
plt.ylabel('Count')
plt.show()



## Find the Dates and Sales Relationship
print(df.head())
# =============================================================================
#    Store       Date  Weekly_Sales  Holiday_Flag  Temp_Celsius  Unemployment
# 0      1 2010-02-05    1643690.90             0     -8.494444         8.106
# 1      1 2010-02-12    1641957.44             1    -10.605556         8.106
# 2      1 2010-02-19    1611968.17             0     -9.816667         8.106
# 3      1 2010-02-26    1409727.59             0     -6.094444         8.106
# 4      1 2010-03-05    1554806.68             0     -6.166667         8.10
# =============================================================================

## We'll be using a new dataframe in the following steps but below is a way we can set a datetime column as our index and drop generic numeric int index value set to dataframe when initially created

df_orig_dtidx = df.iloc[:10, :].copy()
df_orig_dtidx.set_index('Date', drop=True, inplace=True)
# =============================================================================
# print(df_orig_dtidx.head())
#             Store  Weekly_Sales  Holiday_Flag  Temp_Celsius  Unemployment
# Date                                                                     
# 2010-02-05      1    1643690.90             0     -8.494444         8.106
# 2010-02-12      1    1641957.44             1    -10.605556         8.106
# 2010-02-19      1    1611968.17             0     -9.816667         8.106
# 2010-02-26      1    1409727.59             0     -6.094444         8.106
# 2010-03-05      1    1554806.68             0     -6.166667         8.106
# =============================================================================


new_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/w_8', index_col=0)
print(new_df.head())
# =============================================================================
#             Store  Weekly_Sales  Holiday_Flag  Temp_Celsius  Unemployment
# Date                                                                     
# 2010-01-10   23.0  9.386639e+05           0.0      6.815556      8.475289
# 2010-02-04   23.0  1.120530e+06           0.0     -2.488395      8.497711
# 2010-02-07   23.0  1.087055e+06           0.0     10.851852      8.428578
# 2010-02-19   23.0  1.072822e+06           0.0    -11.044568      8.619311
# 2010-02-26   23.0  9.770794e+05           0.0    -10.198025      8.619311
# =============================================================================
print(new_df.index)
# =============================================================================
# Index(['2010-01-10', '2010-02-04', '2010-02-07', '2010-02-19', '2010-02-26',
#        '2010-03-09', '2010-03-12', '2010-03-19', '2010-03-26', '2010-04-06',
#        ...
#        '2012-09-03', '2012-09-14', '2012-09-21', '2012-09-28', '2012-10-02',
#        '2012-10-08', '2012-10-19', '2012-10-26', '2012-11-05', '2012-12-10'],
#       dtype='object', name='Date', length=143)
# =============================================================================

## Transform index type to datetime object
new_df.index = pd.to_datetime(new_df.index)
print(new_df.index)
# =============================================================================
# DatetimeIndex(['2010-01-10', '2010-02-04', '2010-02-07', '2010-02-19',
#                '2010-02-26', '2010-03-09', '2010-03-12', '2010-03-19',
#                '2010-03-26', '2010-04-06',
#                ...
#                '2012-09-03', '2012-09-14', '2012-09-21', '2012-09-28',
#                '2012-10-02', '2012-10-08', '2012-10-19', '2012-10-26',
#                '2012-11-05', '2012-12-10'],
#               dtype='datetime64[ns]', name='Date', length=143, freq=None)
# =============================================================================

# Extract only 2010th year
data = new_df.loc[new_df.index.year == 2010]
#print(len(data))

# Create Figure and Axes objects
fig, ax = plt.subplots()
# Initialize the plot
ax.plot(data.index, data['Weekly_Sales'] , linestyle = 'solid')

# Set custom labels on axis
ax.set_ylabel('Sales')
ax.set_xlabel("Dates")

plt.title("Sales VS Date Chart")
plt.ticklabel_format(style='plain', axis='y')
# Output the plot
plt.show()




## Deal with Holiday's Impact
# =============================================================================
# To add more practice to this project, you are going to work with the same dataset as in the previous chapter, 
# but the dates now aren't indices
# 
# Holiday_Flag , you can see two different values 1 and 0, 1 means holiday, and 0 means that it was a regular day.
# =============================================================================


df_holiday = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/w_8')
print(df_holiday.head())
# =============================================================================
#          Date  Store  Weekly_Sales  Holiday_Flag  Temp_Celsius  Unemployment
# 0  2010-01-10   23.0  9.386639e+05           0.0      6.815556      8.475289
# 1  2010-02-04   23.0  1.120530e+06           0.0     -2.488395      8.497711
# 2  2010-02-07   23.0  1.087055e+06           0.0     10.851852      8.428578
# 3  2010-02-19   23.0  1.072822e+06           0.0    -11.044568      8.619311
# 4  2010-02-26   23.0  9.770794e+05           0.0    -10.198025      8.619311
# =============================================================================

# =============================================================================
# Build a scatter plot and use grouping.Follow the algorithm to receive the plot, in which the relationship between sales 
# and date is presented, and holidays colored especially:
# =============================================================================

holidays = df_holiday['Holiday_Flag'].unique() # [0. 1.]

df_holiday['Date'] = pd.to_datetime(df_holiday['Date'])
fig, ax = plt.subplots()

colors = ["r", "g"]
# Extract unique values from the column 'Holiday_Flag'
holidays = df_holiday['Holiday_Flag'].unique()

for i in range(len(colors)):
  # Apply the required condition
  indices = df_holiday['Holiday_Flag'] == holidays[i] # boolean series for 0 or 1 and subsetting the holiday flag rows
  # Create Scatter plot for found rows in boolean series passed to dataframe to subset on (indices is a boolean series checking if the value of the flag is equal to 1 or 0)
  # only two iterations for loop which will add scatter plots to ax instance
  ax.scatter(df_holiday[indices]['Date'], df_holiday[indices]['Weekly_Sales'], c = colors[i], label = 'Non Holiday' if holidays[i] == 0 else 'Holiday')


# Alter Legend to Non Numeric Values
# plt.legend(labels=['Non Holiday', 'Holiday'])

# Display legend
plt.legend()

plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Weekly Sales Amounts $')
plt.title('Weekly Sales Amount for Non Holidays & Holidays')
# Output the plot
plt.show()




## Influence of Temperature
# =============================================================================
# # Your task here is to find the impact of temperature on the number of sales using colormap om scatter plot
# =============================================================================
# Ð¡reate Figure and Axes objects
fig, ax = plt.subplots()
# Initialize the plot
plot = ax.scatter(df['Date'], df['Weekly_Sales'], c = df['Temp_Celsius'], cmap = 'bwr')

# Add labels and title
ax.set(xlabel = 'Dates' , ylabel = 'Sales' , title = 'Relationship')
# Display the legend
legend = fig.colorbar(plot)
legend.ax.set_xlabel("Temperature")

# Display the plot
plt.ticklabel_format(style='plain', axis='y')
plt.show()



## Find the Temperature and Sales Relationship
# =============================================================================
# You're already noticed that somehow temperature affects weekly sales, 
# but your task here is to find out if there is a strong relationship between the number of degrees and the number of sales
# =============================================================================


fig, ax = plt.subplots()
# Initialize the plot
ax.scatter(df['Temp_Celsius'], df['Weekly_Sales'])
# Define set() function
ax.set(xlabel = 'Temperature', ylabel = 'Sales',
      title = 'Relationship', xlim = (-20, 20) , ylim = (0, 3500000))

plt.ticklabel_format(style='plain', axis='y')
plt.show()
print(df[['Temp_Celsius', 'Weekly_Sales']].corr())
# =============================================================================
# Correlation
#               Temp_Celsius  Weekly_Sales
# Temp_Celsius      1.000000     -0.045063
# Weekly_Sales     -0.045063      1.000000
# =============================================================================
# =============================================================================
# Store  Weekly_Sales  Holiday_Flag  Temp_Celsius  Unemployment
# Store         1.000000     -0.333101      0.003503     -0.027488      0.222829
# Weekly_Sales -0.333101      1.000000      0.025309     -0.045063     -0.104245
# Holiday_Flag  0.003503      0.025309      1.000000     -0.155315      0.012377
# Temp_Celsius -0.027488     -0.045063     -0.155315      1.000000      0.099427
# Unemployment  0.222829     -0.104245      0.012377      0.099427      1.000000
# =============================================================================

































































































