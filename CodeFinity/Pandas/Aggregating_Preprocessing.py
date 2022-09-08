#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:23:45 2022

@author: craigrupp
"""
import pandas as pd
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)
data_flights = data[['Flight', 'Delay']].groupby('Flight').count()
print(data_flights.head())
mean = data[['Flight', 'Delay']].groupby('Flight').mean()
median = data[['Flight', 'Delay']].groupby('Flight').apply('median')
sum_delay_flights = data[['Flight', 'Delay']].groupby('Flight').apply('sum')
min_delay = data[['Flight', 'Delay']].groupby('Flight').apply('min')
max_delay = data[['Flight', 'Delay']].groupby('Flight').apply('max')

mean
# =============================================================================
# data[['Flight', 'Delay']].groupby('Flight').count()
# 
# data[['Flight', 'Delay']] - columns you will work on, including the columns you will group.
# groupby('Flight') - here, 'Flight' is an argument of the function .groupby(). 
#   It is the name of the column by which you will group. 
#   So, in our case, if rows of the data set have the same value in the column 'Flight', they will relate to one group. 
#   Then, due to the function .count() that counts the rows, our function will calculate the numbers of rows of the column 
#   'Delay' that have the same value in the column 'Flight' 
#   Note, this doesn't count the boolean like value 1 or 0 to indicate the flight row instance having a delay of 1 or 0
#   It's simply the count of rows for each flight
# =============================================================================
hey = data[['Flight', 'Delay']]
hey['Flight'].value_counts()
hey[hey['Flight'] == 1]



# =============================================================================
# Groupby Multiple Columns
# Order is imperative

# Below will group by the flight #, then Airline's that share that flight # and the count for each Airline's instance of that flight # 
# =============================================================================

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)
data_flights = data[['Flight', 'Delay', 'Airline']].groupby(['Flight', 'Airline']).count()
print(data_flights.head(10))


# =============================================================================
# Group data:
# Extract columns 'AirportFrom', 'DayOfWeek' and 'Time' from data(in this order).
# Apply the .groupby() function to the previous columns.
# Within the .groupby() function, put columns 'AirportFrom' and 'DayOfWeek'; the order is crucial.
# Calculate the mean value of the column 'Time'.
# =============================================================================
# Few different approaches here for the same results with chaining on the groupedby dataframe
data[['AirportFrom', 'DayOfWeek', 'Time']].groupby(['AirportFrom', 'DayOfWeek']).mean('Time')
data[['AirportFrom', 'DayOfWeek', 'Time']].groupby(['AirportFrom', 'DayOfWeek']).apply('mean')
data[['AirportFrom', 'DayOfWeek', 'Time']].groupby(['AirportFrom', 'DayOfWeek']).agg(['mean', 'median'])

# Only getting mean so just using the mean
# Group data
data_flights = data[['AirportFrom', 'DayOfWeek', 'Time']].groupby(['AirportFrom', 'DayOfWeek']).mean('Time')

# Output the first 10 rows of the data set
print(data_flights.head(10))


# =============================================================================
# Look at the column 'Length'; here, we have the flight length in minutes. 
# Imagine we want to calculate the maximum time in hours for items having the same value in the 'Flight' column and then 'Airline'. 
# So, to do it, we can calculate the maximum value of the column 'Length' for each group key and then divide it by 60
# =============================================================================

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)
data_flights = data[['Flight', 'Airline', 'Length']].groupby(['Flight', 'Airline']).apply(lambda x: x['Length'].max()/60)
print(data_flights.head(10))


data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)
data_flights = data.groupby('Airline').agg({'Delay': 'count', 'Length': ['min', 'max']})
print(data_flights.head(10))


# Use agg function to pass dictionary of operations to perform on grouped by dataframe
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)

# Group data
data_flights = data.groupby(['AirportFrom', 'AirportTo']).agg({'Time': ['mean', 'max'], 'Length': 'median'})

print(data_flights.head(10))



# =============================================================================
# Pivot Table
# Python has an analog of the .groupby() function that can lead to the same result
# =============================================================================


data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)

# The code using .groupby()
data_flights_1 = data[['Length', 'Flight']].groupby('Flight').mean()
data_flights_1
# The same code using .groupby()
data_flights_2 = data[['Length', 'Flight']].groupby('Flight').agg('mean')
data_flights_2

# The same output using .pivot_table()
data_flights_3 = pd.pivot_table(data, values = 'Length',
index = 'Flight',
aggfunc = 'mean')
data_flights_3


# =============================================================================
# Pivot Table Explained

# index : is an argument to which you assign the name of column or 
# columns on which you want to group. If you want to group by several columns, put them into the list; 
# the order is crucial, like in the .groupby() function.

# values :  to the argument values we assign columns having the same group, for which we will apply the calculation of the average, maximum, etc. 
# If you want to group by several columns, put them into the list; the order isn't crucial.
# Think of as the aggregate column we want to perform our agg operation on from the grouped by variable
# Ex: For each flight there will be a length measured and for each same flight we can group these together to get the mean off all lengths for that flight

#aggfunc : the same as agg in the .groupby() function, aggfunc has completely the same syntax as agg. 
# Thus, you can put several functions here by putting them into the list to specify functions for different columns using curly brackets.
# =============================================================================

# =============================================================================
# Your task here is to practice using pivot tables. 
# Depending on the airline and the airport from which the flight started, 
# calculate the number of delays and the minimum and maximum length of the flight
# =============================================================================

flights_pivot = data.copy()
flights_pivot.info()
flights_pivot['Delay'].unique()

#Count Boolean Delay Column use in aggfunc!
def count_delay(series):
    total_delay = 0
    for dl in series.values:
        if dl == 1:
            total_delay += 1
    return total_delay

fp = pd.pivot_table(data=flights_pivot, index=['Airline', 'AirportFrom'], values=['Delay', 'Length'], aggfunc={'Delay': count_delay, 'Length': ['min', 'max']})
print(fp)
first_line = flights_pivot.loc[(flights_pivot['Airline'] == '9E') & (flights_pivot['AirportFrom'] == 'ABE')]
len(first_line)
first_line[['Delay', 'Length']]






