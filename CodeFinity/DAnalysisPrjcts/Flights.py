#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:57:40 2022

@author: craigrupp
"""

# Import the library
import pandas as pd

# Load data
flights = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/9ac68942-3d74-433b-abb9-4550ae491761/flights_sample.csv', index_col = 0)

# Print shape of flights
print(flights.shape)

# Print information of flights columns
print(flights.info())

print(flights.head())


## Modify / Combine Date
# =============================================================================
# Let's use the American format of time: month/day/year. 
# To do it, we will concatenate values from MONTH, DAY, and YEAR columns, separated by /. 
# We will define the lambda function for this.
# Values are all integers currently
# =============================================================================

# Define function
to_date = lambda x: x["MONTH"].astype(str) + "/" + x["DAY"].astype(str) + "/" + x["YEAR"].astype(str)

# Apply function to flights data - lambda method iterating over frame's rows
flights['date'] = to_date(flights)

# Explore the last 5 observations of new column
print(flights['date'].tail(5))
# =============================================================================
# 3172039    7/17/2015
# 2127212    5/15/2015
# 2859979    6/29/2015
# 3659266    8/15/2015
# 4299913    9/25/2015
# Name: date, dtype: object
# =============================================================================


## Quick Conversion and relvant datetime column

# Convert column into date type
flights['date_conv'] = pd.to_datetime(flights["date"], format = '%m/%d/%Y')

# Print minimal and maximal converted dates
print(f"The earliest date in dataset: {min(flights['date_conv'])}")
print(f"The latest date in dataset: {max(flights['date_conv'])}")
# =============================================================================
# The earliest date in dataset: 2015-01-01 00:00:00
# The latest date in dataset: 2015-12-31 00:00:00
# =============================================================================

# Print number of unqiue dates in dataset
print(f"There are {len(flights['date_conv'].unique())} unique dates in dataset") 

# =============================================================================
# The earliest date in dataset: 2015-01-01 00:00:00
# The latest date in dataset: 2015-12-31 00:00:00
# There are 365 unique dates in dataset
# =============================================================================



## Most Popular Day of the Week to Fly

# Add new column with days of week
flights['day_of_week'] = flights['date_conv'].dt.day_name()
print(flights['day_of_week'].value_counts())

# Days of week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Build histogram for days of week (Interesting way to index a series)
flights["day_of_week"].value_counts()[days].plot(kind = 'bar')


# Estimating Time
# =============================================================================
# Each flight has a 'taxi' phase, which refers to the time before takeoff or after landing. 
# Usually, it refers to the movement of an aircraft on the ground.
# 
# In this dataset we have two columns that can help us to 
# evaluate these times: 
#     DEPARTURE_TIME - the time a plane finished passenger boarding and started moving on the ground (as float, in the format hhmm.0) 
#     WHEELS_OFF - the time when a plane transitioned from moving along the ground to flying in the air (the same format).
# 
# Seems like we can simply subtract the WHEELS_OFF column and DEPARTURE_TIME. 
# But there are some inconveniences. Since both of these columns are float64, 
# it means that if the first digit in the hour is 0, then it won't be displayed. 
# We somehow need to add redundant zeros and place a colon sign as an hour/minute separator.
# =============================================================================

print(flights[['DEPARTURE_TIME', 'WHEELS_OFF']].head())

# =============================================================================
#          DEPARTURE_TIME  WHEELS_OFF
# 2464670          1621.0      1631.0
# 3928603          1253.0      1310.0
# 3102055          2014.0      2024.0
# 5049064           721.0       733.0
# 4361783          1344.0      1406.0
# =============================================================================
#car_specs = car_specs.assign(year = car_specs.car_full_nm.str.slice(start = -5, stop = -1) )

flights.dropna(subset = ['DEPARTURE_TIME', 'WHEELS_OFF'], inplace = True)

value_check_dep = lambda x: x['DEPARTURE_TIME'].astype(str)
value_check_whl = lambda x: x['WHEELS_OFF'].astype(str)

flights['dep_check'] = value_check_dep(flights)
flights['whls_check'] = value_check_whl(flights)

print(flights[['DEPARTURE_TIME', 'dep_check', 'WHEELS_OFF', 'whls_check']].head())
print(flights[['DEPARTURE_TIME', 'dep_check', 'WHEELS_OFF', 'whls_check']].dtypes)

flights = flights.assign(dep_check = flights['dep_check'].str.slice(-1))
flights = flights.assign(whls_check = flights['whls_check'].str.slice(-1))
print(flights.columns.tolist())
print(flights.head(2))
# =============================================================================
#   The dep_check and whls_check below shows what our head hints at here (all float decimal values are 0 for both columns for our operation)
#          YEAR  MONTH  DAY  ... day_of_week dep_check  whls_check
# 2464670  2015      6    5  ...      Friday         0           0
# 3928603  2015      9    1  ...     Tuesday         0           0
# =============================================================================

#flights.assign(hell = flights['DEPARTURE_TIME'].str.slice(-1), inplace=True) # Can only use .str accessor with string values!

print(flights['dep_check'].value_counts())
print(flights['whls_check'].value_counts())
# =============================================================================
# Zeros! only Zeros!

# 0    114623
# Name: dep_check, dtype: int64
# 0    114623
# Name: whls_check, dtype: int64
# =============================================================================

## Let's take the steps to convert departure and wheels off times into datetime format.
# =============================================================================
# Length of string	Example	Way to solve	Resulted from example
# 4 : 	1540	Concatenate the first 2 characters, colon, and the last two	15:40
# 4	:   2400	Replace with the 00:00	00:00
# 3	:   725	    Concatenate 0, the first symbol, colon, and the last two	07:25
# 2	:   45	    Concatenate 00:, and the entire string	00:45
# 1	:   5	    Conatenate 00:0, and the symbol left	00:05
# =============================================================================
# Implement to_time function
def to_time(x):
    # Remove .0 parts using .replace
    res = str(x).replace('.0', '')
    if len(res) == 1:
        # Concatenate "00:0" and res
        return '00:0' + res
    elif len(res) == 2:
        # Concatenate "00:" and res
        return '00:' + res
    elif len(res) == 3:
        return '0' + res[0] + ":" + res[1:]
    elif res == '2400':
        # Return string "00:00"
        return "00:00"
    else:
        # Add colon sign
        return res[:2] + ':' + res[2:]

# Replacing the columns values   
flights['DEPARTURE_TIME'] = flights['date_conv'].astype(str) + ' ' + flights['DEPARTURE_TIME'].apply(to_time)
flights['WHEELS_OFF'] = flights['date_conv'].astype(str) + " " + flights['WHEELS_OFF'].apply(to_time)

print(flights['date_conv'].head(2))
# =============================================================================
# 2464670   2015-06-05
# 3928603   2015-09-01
# Name: date_conv, dtype: datetime64[ns]

# Part of value used to create a valide timestamp with the departure_time and wheels_off time modified with the to_time function
# =============================================================================


# Print the first 5 observations of DEPARTURE_TIME column
print(flights['DEPARTURE_TIME'].head(5))

# =============================================================================
# 2464670    2015-06-05 16:21
# 3928603    2015-09-01 12:53
# 3102055    2015-07-13 20:14
# 5049064    2015-11-12 07:21
# 4361783    2015-09-29 13:44
# Name: DEPARTURE_TIME, dtype: object
# =============================================================================



# Convert columns into datetime format (transformed value above for both columns still an object : 24 Hour )
flights['DEPARTURE_TIME'] = pd.to_datetime(flights['DEPARTURE_TIME'], format = '%Y-%m-%d %H:%M')
flights['WHEELS_OFF'] = pd.to_datetime(flights['WHEELS_OFF'], format = '%Y-%m-%d %H:%M')

# Build the histogram for time durations
((flights['WHEELS_OFF'] - flights['DEPARTURE_TIME']).dt.total_seconds()/60).hist()


# Correcting Negative Taxi Times
print(flights['WHEELS_OFF'].dtype)

# Define function
def date_corr(x):
    # Compare the number of seconds with 0
    if (x["WHEELS_OFF"] - x["DEPARTURE_TIME"]).total_seconds() < 0:
        return x['WHEELS_OFF'] + pd.Timedelta('1 day')
    else:
        return x['WHEELS_OFF']

# Apply function to column
flights['WHEELS_OFF'] = flights.apply(lambda x: date_corr(x), axis = 1)

# Build the histogram for time durations
((flights['WHEELS_OFF'] - flights['DEPARTURE_TIME']).dt.total_seconds()/60).hist()



## Calculating Arrival Time
# =============================================================================
# Now let's calculate the actual arrival times. We can do it by using 'WHEELS_OFF', 'AIR_TIME', and 'TAXI_IN' columns. 
# There we need to add to the datetime column 'WHEELS_OFF' rest of the columns as timedelta.
# =============================================================================

# Calculate the arrival time
flights['ARRIVAL_TIME'] = flights['WHEELS_OFF'] + pd.to_timedelta(flights['AIR_TIME'], unit = 'm') + pd.to_timedelta(flights['TAXI_IN'], unit = 'm')
        
# Print the last 5 arrival times
print(flights['ARRIVAL_TIME'].tail(5))


## Arrival Times

# Create column for arrival delays
flights['ARRIVAL_DELAY'] = flights['ARRIVAL_TIME'] - flights['SCHEDULED_ARRIVAL']

# Build the histogram
(flights['ARRIVAL_DELAY'].dt.total_seconds()/60).hist()


# Fix Outliers
# Define function
def date_corr_two(x):
   if (x["ARRIVAL_TIME"] - x["SCHEDULED_ARRIVAL"]).total_seconds()/60 > 1000:
        return x['ARRIVAL_TIME'] - pd.Timedelta('1 day')
   elif (x["ARRIVAL_TIME"] - x["SCHEDULED_ARRIVAL"]).total_seconds()/60 < -1000:
        return x['ARRIVAL_TIME'] + pd.Timedelta('1 day')
   else:
        return x['ARRIVAL_TIME']

# Apply function to column
flights['ARRIVAL_TIME'] = flights.apply(lambda x: date_corr_two(x), axis = 1)

# Build the histogram
((flights['ARRIVAL_TIME'] - flights['SCHEDULED_ARRIVAL']).dt.total_seconds()/60).hist()


# Create Figure and Axes objects
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Build scatter plot
ax.scatter(x = flights['DISTANCE'], y = flights['ARRIVAL_DELAY'])

# Customize the plot
ax.set(xlabel = 'Distance', ylabel = 'Delay')

# Display the plot
plt.show()


# Create Figure and Axes objects
fig, ax = plt.subplots()

# Filter to only delays columns
delays = flights[['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']]

# Build bar chart
for i in delays.columns:
    ind = (flights[i].isna() == False) & (flights[i] != 0)
    y = flights.loc[ind][i].sum()/len(flights.loc[ind][i])
    ax.bar(x = i.replace('_DELAY', ""), height = y)

# Customize and display the plot
ax.set(xlabel = 'Delay reason', ylabel = 'Average delay (minutes)')
plt.show()



































