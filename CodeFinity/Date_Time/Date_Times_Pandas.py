#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:46:30 2022

@author: craigrupp
"""

import pandas as pd
from datetime import timedelta

# Loading dataset
url = 'https://drive.google.com/uc?id=1gTwOHgdPjGRDltZgDnccDwAPsv736q9W'
df = pd.read_csv(url)

print(df.head())
# =============================================================================
#    id                vendor_id  ... dist_meters wait_sec
# 0   1  México DF Taxi de Sitio  ...       12373      242
# 1   2     México DF Taxi Libre  ...        1700      461
# 2   3     México DF Taxi Libre  ...        2848      129
# 3   4     México DF Taxi Libre  ...        1409      106
# 4   5     México DF Taxi Libre  ...        1567       85
# =============================================================================

print(df.columns)

# =============================================================================
# Index(['id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime',
#        'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
#        'dropoff_latitude', 'store_and_fwd_flag', 'trip_duration',
#        'dist_meters', 'wait_sec'],
#       dtype='object')
# =============================================================================

print(df.info())
# =============================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 12694 entries, 0 to 12693
# Data columns (total 12 columns):
#  #   Column              Non-Null Count  Dtype  
# ---  ------              --------------  -----  
#  0   id                  12694 non-null  int64  
#  1   vendor_id           12694 non-null  object 
#  2   pickup_datetime     12694 non-null  object 
#  3   dropoff_datetime    12694 non-null  object 
#  4   pickup_longitude    12694 non-null  float64
#  5   pickup_latitude     12694 non-null  float64
#  6   dropoff_longitude   12694 non-null  float64
#  7   dropoff_latitude    12694 non-null  float64
#  8   store_and_fwd_flag  12694 non-null  object 
#  9   trip_duration       12694 non-null  int64  
#  10  dist_meters         12694 non-null  int64  
#  11  wait_sec            12694 non-null  int64  
# dtypes: float64(4), int64(4), object(4)
# memory usage: 1.2+ MB
# =============================================================================

# Converting Column types
# =============================================================================
# You might notice, that pickup_datetime and dropoff_datetime columns are recognized as the object type. 
# It means we can not perform the actions we did in the previous sections there.
# =============================================================================
# =============================================================================
# pd.to_datetime(arg, dayfirst = False, yearfirst = False, format = None, exact = True, ...)
# The arguments below are not exhaustive
# arg - is the value(s)/column you want to convert, 
# dayfirst and yearfirst - specify if a parse date with day/year first, 
# format - format of datetime object to parse (like in strptime() - you need to define the used format), 
# exact - if True, require an exact match. 
# All arguments but not arg are optional. 
# If you will not specify a format, it will try to guess.
# =============================================================================
print(df[['pickup_datetime', 'dropoff_datetime']].head(5))
print(df['pickup_datetime'].sort_values(ascending=False).head(2))
# =============================================================================
# 1803    2017-07-20 12:52:00
# 1769    2017-07-20 12:48:41
# Name: pickup_datetime, dtype: object
# =============================================================================
print(df['dropoff_datetime'].sort_values(ascending=False).head(2))
# =============================================================================
# 1803    2017-07-20 12:53:21
# 1769    2017-07-20 12:51:26
# Name: dropoff_datetime, dtype: object
# =============================================================================

# Doesn't appear anything other than a 12 hour clock was used


# Task 1 - get the first pickup datetime
dt_before = df["pickup_datetime"][0]

# Task 2 - convert columns into datetime type
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"], format='%Y-%m-%d %I:%M:%S')

# Task 3 - get the first pickup datetime
dt_after = df["pickup_datetime"][0]

# Comparing results
print(f"Datetime before convertion {dt_before} was type {type(dt_before)}")
print(f"Datetime after convertion {dt_after} is type {type(dt_after)}")

## Datetime before convertion 2016-09-16 07:14:12 was type <class 'str'>
## Datetime after convertion 2016-09-16 07:14:12 is type <class 'pandas._libs.tslibs.timestamps.Timestamp'>



# Challenge: Extreme Trips Durations - Note Here that Dropoff datetimes are after a pickup_datetime so ... yeah
# =============================================================================
# We already have column trip_duration in our dataset, so why do we need to work with datetime objects? 
# Yes, we have, but this number is in seconds, which is not readable at all (since there are 60 seconds in one minute, not 100).
# Let's see if there are outliers in our dataset.
# =============================================================================
# Task 1 - create new column
df['duration'] = df['dropoff_datetime'] - df['pickup_datetime']

# Task 2 - sort dataframe by duration in descending orger
df_sort = df.sort_values('duration', ascending = False)

# Task 3 - print top-5 longest and shortest trips
print("The longest trips:")
print(df_sort.head())
# =============================================================================
# The longest trips:
#           id             vendor_id  ... wait_sec          duration
# 11687  11688       México DF UberX  ...    51500 192 days 07:02:29
# 11767  11768  México DF Taxi Libre  ...    19954  75 days 21:12:44
# 7537    7538   México DF UberBlack  ...      213  64 days 21:55:42
# 486      487  México DF Taxi Libre  ...     4652  62 days 23:46:21
# 367      368  México DF Taxi Libre  ...      213  55 days 22:01:58
# =============================================================================
print("The shortest trips:")
print(df_sort.tail())
# =============================================================================
# The shortest trips:
#         id                vendor_id  ... wait_sec          duration
# 2043  2044  México DF Taxi de Sitio  ...        1 -1 days +12:00:14
# 1467  1468  México DF Taxi de Sitio  ...     4203 -1 days +12:00:12
# 617    618     México DF Radio Taxi  ...        9 -1 days +12:00:10
# 5072  5073     México DF Taxi Libre  ...        0 -1 days +12:00:07
# 6888  6889     México DF Taxi Libre  ...      179 -1 days +12:00:04
# =============================================================================


# Challenge : Keep Digging
# =============================================================================
# As you noticed from the previous chapter, there are trips with negative and extremely huge durations (like more than 50 days). 
# Surely this data can not be real, and we need to fix it if we want to go further.
# 
# What is the reason for extremely long trips? 
# Most likely, it happened because some drivers forgot to turn off the taximeter when done with the route. 
# The easiest way to deal with it - is simply to remove them as outliers. 
# We will remove all the observations with durations greater-equal than 2 days

## We can also use the parse_dates arguments when reading in the fill to format the columns when loading in the dataset to our df
# =============================================================================

# Loading dataset and creating duration column
url = 'https://drive.google.com/uc?id=1gTwOHgdPjGRDltZgDnccDwAPsv736q9W'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime'])
df['duration'] = df['dropoff_datetime'] - df['pickup_datetime']

len_before = len(df) # Number of rows in dataset before deleting

# Task 1 - remove extremely long trips
## Notice Syntax here to offset a dataframe by omitting rows found in condition equivalent to not
## df[-(condition)] = rows not found in this conidition
df_outlier_excluded = df[-(df['duration'] >= timedelta(days = 2))]
## Validate df now doesn't contain outliers by ordering the column in descending order (validate first row not greater than 2 days)
print(df.head(2).sort_values('duration', ascending=False))
# =============================================================================
#    id                vendor_id  ... wait_sec        duration
# 0   1  México DF Taxi de Sitio  ...      242 1 days 21:27:28
# 1   2     México DF Taxi Libre  ...      461 0 days 03:55:10
# =============================================================================
## Similar syntax to above but will create new dataframe from original df (with same condition but not use the inverse syntax like above)
df_outliers_gthan = df[df['duration'] >= timedelta(days=2)]
## Validate greater than outliers for sorted values in ascending orders being greater than or equal to 2 days 
print(df_outliers_gthan.head(2).sort_values('duration', ascending=True))
# =============================================================================
#     id                vendor_id  ... wait_sec         duration
# 74  75     México DF Radio Taxi  ...      289  2 days 02:11:45
# 26  27  México DF Taxi de Sitio  ...      136 32 days 06:59:00
# =============================================================================

# Comparing
print(f"Before deleting there were {len_before} rows.")
print(f"After deleting outlier we have {len(df_outlier_excluded)} rows.")
print(f"Ouliers dataframe has the difference : {len(df_outliers_gthan)}")
print(f"Adding the output of each : {len(df_outlier_excluded) + len(df_outliers_gthan)} should be {len(df)}")
# =============================================================================
# Before deleting there were 12694 rows.
# After deleting outlier we have 12402 rows.
# Ouliers dataframe has the difference : 292
# Adding the output of each : 12694 should be 12694
# =============================================================================

# Task 2 - get first 10 trips with negative durations : Use Timedelta
negative_condition = df['duration'] < timedelta(days=0)
print(df_outlier_excluded[(negative_condition)][['pickup_datetime', 'dropoff_datetime', 'duration']].head(10))
# =============================================================================
# 35  2016-09-19 11:47:23 2016-09-19 02:21:19 -1 days +14:33:56
# 67  2016-09-20 12:11:43 2016-09-20 02:15:55 -1 days +14:04:12
# 76  2016-09-20 12:55:00 2016-09-20 01:03:36 -1 days +12:08:36
# 134 2017-04-22 12:38:41 2017-04-22 01:20:13 -1 days +12:41:32
# 233 2017-04-24 12:56:31 2017-04-24 01:06:18 -1 days +12:09:47
# 234 2017-04-24 12:55:12 2017-04-24 01:11:02 -1 days +12:15:50
# 262 2017-04-25 09:19:44 2017-04-25 01:44:55 -1 days +16:25:11
# 302 2017-04-26 08:11:41 2017-04-26 06:51:32 -1 days +22:39:51
# 327 2017-04-28 12:53:57 2017-04-28 01:35:10 -1 days +12:41:13
# 409 2016-08-06 12:55:38 2016-08-06 02:09:20 -1 days +13:13:42
# =============================================================================


# Negative Trip Durations?
# =============================================================================
# # Well, in the last chapter you might notice that for the first 10 rows all the trips started before 13 hours (1 p.m.), 
# # and ended close to 00 hours. What if it's just AM/PM missing? Let's try to check it.
# =============================================================================
# =============================================================================
# How can it be checked? Well, in our dataframe we also have trip_duration column representing the trip duration in seconds. 
# What if we just add this duration to pickup_datetime and compare it with dropoff_datetime?
# =============================================================================

# Loading dataset and modifying duration column - Note this URL/dataset already has an existing 'duration' column
url = 'https://drive.google.com/uc?id=1KoZJyLO791MqW-JICYukrApH4qfiniGG'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime'])
print(df.columns)
print(df.info())
print(df[['pickup_datetime', 'dropoff_datetime', 'duration']].head(2))
df["duration"] = pd.to_timedelta(df["duration"])


# Task 1 - convert trip duration into timedelta type / was an int
##  Do not forget that trip_duration measures in seconds for initial value looking to be converted
df["trip_duration"] = pd.to_timedelta(df["trip_duration"], unit = "S")

# Task 2 - create new_column dropoff_calculated using the initial datetime (pickup_datetime) and new timedelta value for total duration captured for the trip now transformed to timedelta for arithmetic value creation
df["dropoff_calculated"] = df["pickup_datetime"] + df["trip_duration"]

# Task 3 - print first 5 rows with negative durations
print(df[df["duration"] < timedelta(days=0)][["pickup_datetime", 'trip_duration', "dropoff_datetime", "dropoff_calculated"]].head(5))
# =============================================================================
#         pickup_datetime   trip_duration    dropoff_datetime  dropoff_calculated
# 34  2016-09-19 11:47:23 0 days 02:33:56 2016-09-19 02:21:19 2016-09-19 14:21:19
# 66  2016-09-20 12:11:43 0 days 02:04:13 2016-09-20 02:15:55 2016-09-20 14:15:56
# 74  2016-09-20 12:55:00 0 days 00:08:36 2016-09-20 01:03:36 2016-09-20 13:03:36
# 132 2017-04-22 12:38:41 0 days 00:41:32 2017-04-22 01:20:13 2017-04-22 13:20:13
# 231 2017-04-24 12:56:31 0 days 00:09:47 2017-04-24 01:06:18 2017-04-24 13:06:18
# =============================================================================


# =============================================================================
# ## Output above illustrated that the created column dropoff_calculated appears to share the same minute and second values with the
# ## hour value detailing what looks like a misusage of 12-hr formats and 24-hr formats
# =============================================================================

## How Common is This??
## Note new file being used which has our previously created dropoff_calculated column in the raw file

url = 'https://drive.google.com/uc?id=1YV5bKobzYxVAWyB7VlxNH6dmfP4tHBui'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated'])
df = df.iloc[:, 2:].set_index('id')
#print(df[['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated', 'duration']].head(2))
df["duration"] = pd.to_timedelta(df["duration"])
print(df[['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated', 'duration']].head(2))
# =============================================================================
#        pickup_datetime    dropoff_datetime  dropoff_calculated        duration
# id                                                                            
# 1  2016-09-16 07:14:12 2016-09-18 04:41:40 2016-09-17 16:41:41 1 days 21:27:28
# 2  2016-09-18 06:16:33 2016-09-18 10:11:43 2016-09-18 10:11:43 0 days 03:55:10
# =============================================================================
# Task 1 - filter to only rides with negative durations
df_neg = df[df["duration"] < timedelta(days=0)]
print(len(df_neg))
## 478 

# Task 2 - iterate over df_neg rows to find inconsistencies
count = 0
for i, row in df_neg.iterrows():
  # Compare minutes of dropoff_datetime and dropoff_calculated
  if row["dropoff_datetime"].minute != row["dropoff_calculated"].minute:
    # Print these two columns
    print(row[["dropoff_datetime", "dropoff_calculated"]])
    # Task 3 - count number of rows having hour greater-equal than 12
  if row["dropoff_datetime"].hour >= 12:
    count +=1

# Rows produced from minute not matching expected dropoff_calculated (just 2 found)
# =============================================================================
# dropoff_datetime      2017-06-04 04:35:59
# dropoff_calculated    2017-06-04 16:36:00
# Name: 4864, dtype: object
# dropoff_datetime      2016-10-07 06:32:59
# dropoff_calculated    2016-10-07 18:33:00
# =============================================================================

## No found rows for expected/calculated that exceeded 12 
print(f"There are {count} rows in df_neg having hour greater-equal than 12.")
## There are 0 rows in df_neg having hour greater-equal than 12.

