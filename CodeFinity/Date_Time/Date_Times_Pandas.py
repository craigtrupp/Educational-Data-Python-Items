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
# Estimate duration with timeseries object calculation
df['duration'] = df['dropoff_datetime'] - df['pickup_datetime']
print(df['duration'].head(3).sort_values(ascending=False))
print(df['duration'].head(3).sort_values(ascending=True))

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
# Validate dataframe with negative durations were caught with shortest negative duration at the top
print(df_outlier_excluded[(negative_condition)][['pickup_datetime', 'dropoff_datetime', 'duration']].sort_values('duration', ascending=True).head(3))
# =============================================================================
#          pickup_datetime    dropoff_datetime          duration
# 8912 2017-05-27 12:59:24 2017-05-27 01:00:09 -1 days +12:00:45
# 5669 2016-12-26 12:59:36 2016-12-26 01:01:24 -1 days +12:01:48
# 9930 2016-07-22 12:58:15 2016-07-22 01:01:16 -1 days +12:03:01
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
# =============================================================================
# Index(['Unnamed: 0', 'id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime',
#        'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
#        'dropoff_latitude', 'store_and_fwd_flag', 'trip_duration',
#        'dist_meters', 'wait_sec', 'duration'],
# =============================================================================
print(df.info())
# =============================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 12402 entries, 0 to 12401
# Data columns (total 14 columns):
#  #   Column              Non-Null Count  Dtype         
# ---  ------              --------------  -----         
#  0   Unnamed: 0          12402 non-null  int64         
#  1   id                  12402 non-null  int64         
#  2   vendor_id           12402 non-null  object        
#  3   pickup_datetime     12402 non-null  datetime64[ns]
#  4   dropoff_datetime    12402 non-null  datetime64[ns]
#  5   pickup_longitude    12402 non-null  float64       
#  6   pickup_latitude     12402 non-null  float64       
#  7   dropoff_longitude   12402 non-null  float64       
#  8   dropoff_latitude    12402 non-null  float64       
#  9   store_and_fwd_flag  12402 non-null  object        
#  10  trip_duration       12402 non-null  int64         
#  11  dist_meters         12402 non-null  int64         
#  12  wait_sec            12402 non-null  int64         
#  13  duration            12402 non-null  object 
# =============================================================================
print(df[['pickup_datetime', 'dropoff_datetime', 'duration', 'trip_duration']].head(2))
# =============================================================================
#       pickup_datetime    dropoff_datetime         duration  trip_duration
# 0 2016-09-16 07:14:12 2016-09-18 04:41:40  1 days 21:27:28         120449
# 1 2016-09-18 06:16:33 2016-09-18 10:11:43  0 days 03:55:10          14110
# =============================================================================
print(df['pickup_datetime'][0] + df['trip_duration'][0])

## Addition/subtraction of integers and integer-arrays with Timestamp is no longer supported.  Instead of adding/subtracting `n`, use `n * obj.freq`
# Duration current object dtypes looks like it could be approximated by pandas function / let's make a datetime so we can see what negative durations exist
df["duration"] = pd.to_timedelta(df["duration"])

# Task 1 - convert trip duration into timedelta type / was an int
##  Do not forget that trip_duration measures in seconds for initial value looking to be converted
df["trip_duration"] = pd.to_timedelta(df["trip_duration"], unit = "S")
print(df[['pickup_datetime', 'dropoff_datetime', 'duration', 'trip_duration']].head(2))
# =============================================================================
#       pickup_datetime    dropoff_datetime        duration   trip_duration
# 0 2016-09-16 07:14:12 2016-09-18 04:41:40 1 days 21:27:28 1 days 09:27:29
# 1 2016-09-18 06:16:33 2016-09-18 10:11:43 0 days 03:55:10 0 days 03:55:10
# 
# =============================================================================
# Task 2 - create new_column dropoff_calculated using the initial datetime (pickup_datetime) and new timedelta value for total duration captured for the trip now transformed to timedelta for arithmetic value creation
df["dropoff_calculated"] = df["pickup_datetime"] + df["trip_duration"]
print(df[['pickup_datetime', 'dropoff_datetime', 'trip_duration','dropoff_calculated']].head(2))
# Note below that the dropoff calculated (w/24 Hour) shares minutes and seconds and 1 day and 9 hours would be around 4-5 pm as the dropoff calculates predicts
# based on the total seconds new timedelta value being added to the initial datestamp column (pickup_datetime)
# =============================================================================
#       pickup_datetime    dropoff_datetime   trip_duration  dropoff_calculated
# 0 2016-09-16 07:14:12 2016-09-18 04:41:40 1 days 09:27:29 2016-09-17 16:41:41
# 1 2016-09-18 06:16:33 2016-09-18 10:11:43 0 days 03:55:10 2016-09-18 10:11:43
# =============================================================================

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
df["duration"] = pd.to_timedelta(df["duration"])
print(df[['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated', 'duration']].head(2))
print(df.info())
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


## Challenge : Fixing The Issue
# =============================================================================
# Well, in the last chapter you saw, that there were only two rides with negative durations where minutes in both columns were different. 
# But if paid your attention to seconds, you might notice, that that were the minute ending and starting (59 seconds, and 00 respectively). 
# It means that all the inconsistencies can be interpreted as misuages of 12 and 24-hour formats.
# =============================================================================
# =============================================================================
# one of the ways to replace values in dataframe based on some condition - .where function.
# Col name is the one to update based on where condition of another column
# df['col_name'].where(~(condition), inplace = True, other = values_to_replace)
# =============================================================================

# Loading dataset, creating duration column, and filtering to negative durations
url = 'https://drive.google.com/uc?id=1YV5bKobzYxVAWyB7VlxNH6dmfP4tHBui'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated'])
df["duration"] = pd.to_timedelta(df["duration"])
df = df.iloc[:, 2:].set_index('id')

# Let's use that Where and Check it Out a Bit
df_where = df.copy()
print(df_where.head(2))
# find some negative durations with where check on timedelta duration column
print(df_where[(df_where['duration'] < timedelta(days=0))][['dropoff_datetime', 'dropoff_calculated', 'duration']].sort_values('duration', ascending=True).head(2))
# Here is a sample of dropoff_datetime values with negative durations that will want to update the dropoff_datetime column for (12 hour clock misusage)
# =============================================================================
#         dropoff_datetime  dropoff_calculated          duration
# id                                                            
# 8913 2017-05-27 01:00:09 2017-05-27 13:00:09 -1 days +12:00:45
# 5670 2016-12-26 01:01:24 2016-12-26 13:01:24 -1 days +12:01:48
# =============================================================================
# Task 1: add 12 hours to dropoff duration for negative durations
df['dropoff_datetime'].where(~(df['duration'] < timedelta(0)), other = df['dropoff_datetime'] + timedelta(hours = 12), inplace = True)
print(df[['dropoff_datetime', 'dropoff_calculated', 'duration']].sort_values('duration', ascending=True).head(2))
# Validate dropoff_datetime had timedelta value added correctly to it's existing datetime object : dropoff_datetime : datetime64[ns] 
# =============================================================================
#         dropoff_datetime  dropoff_calculated          duration
# id                                                            
# 8913 2017-05-27 13:00:09 2017-05-27 13:00:09 -1 days +12:00:45
# 5670 2016-12-26 13:01:24 2016-12-26 13:01:24 -1 days +12:01:48
# =============================================================================
# Task 2: recalculate duration column (Operation performed between two datetime dtype columns)
df['duration'] = df['dropoff_datetime'] - df['pickup_datetime']

# Task 3: inspect first 10 rows with negative duration (Following our update of the duration value with the dropoff_datetime : let's see if we still have any negative durations : fingers crossed we don't)
print(df[df['duration'] < timedelta(0)][["pickup_datetime", "dropoff_datetime", "trip_duration", "dropoff_calculated"]].head(10))
# =============================================================================
# Empty DataFrame
# Columns: [pickup_datetime, dropoff_datetime, trip_duration, dropoff_calculated]
# Index: []
# =============================================================================
## Huzzah we dont!



# Challenge: Average Metrics Across Taxi Types
# =============================================================================
# As for now, we have our dataset cleared from abnormally long rides and rides with ending time preceded starting. 
# As we investigated, it happened because of misusage of 12 and 24-hour formats.
# =============================================================================
# Loading dataset, creating duration column
url = 'https://drive.google.com/uc?id=1pQCA5C4Yvm86rjUIneefI31LNfoywtrU'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated'])
df["duration"] = pd.to_timedelta(df["duration"])
df = df.iloc[:, 3:].set_index('id')
print(df.info())
# =============================================================================
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 12402 entries, 1 to 12694
# Data columns (total 13 columns):
#  #   Column              Non-Null Count  Dtype          
# ---  ------              --------------  -----          
#  0   vendor_id           12402 non-null  object         
#  1   pickup_datetime     12402 non-null  datetime64[ns] 
#  2   dropoff_datetime    12402 non-null  datetime64[ns] 
#  3   pickup_longitude    12402 non-null  float64        
#  4   pickup_latitude     12402 non-null  float64        
#  5   dropoff_longitude   12402 non-null  float64        
#  6   dropoff_latitude    12402 non-null  float64        
#  7   store_and_fwd_flag  12402 non-null  object         
#  8   trip_duration       12402 non-null  object         
#  9   dist_meters         12402 non-null  int64          
#  10  wait_sec            12402 non-null  int64          
#  11  duration            12402 non-null  timedelta64[ns]
#  12  dropoff_calculated  12402 non-null  datetime64[ns] 
# dtypes: datetime64[ns](3), float64(4), int64(2), object(3), timedelta64[ns](1)
# =============================================================================
print(df[['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated', 'duration']].head(5))
# =============================================================================
#        pickup_datetime    dropoff_datetime  dropoff_calculated        duration
# id                                                                            
# 1  2016-09-16 07:14:12 2016-09-18 04:41:40 2016-09-17 16:41:41 1 days 21:27:28
# 2  2016-09-18 06:16:33 2016-09-18 10:11:43 2016-09-18 10:11:43 0 days 03:55:10
# 3  2016-09-18 10:11:50 2016-09-18 10:23:11 2016-09-18 10:23:11 0 days 00:11:21
# 4  2016-09-18 10:23:38 2016-09-18 10:30:53 2016-09-18 10:30:54 0 days 00:07:15
# 5  2016-09-18 10:44:18 2016-09-18 10:51:40 2016-09-18 10:51:40 0 days 00:07:22
# =============================================================================

# Defining functions
avg_m = lambda x: str(round(x/1000, 2)) + ' km'
avg_dur = lambda x: pd.to_timedelta(round(x, 0), unit = "S")

# Task 1 - use total_seconds method to duration column (timedelta object method)
df['duration'] = df['duration'].map(lambda x: x.total_seconds())
print(df[['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated', 'duration']].head(5))
# =============================================================================
#        pickup_datetime    dropoff_datetime  dropoff_calculated  duration
# id                                                                      
# 1  2016-09-16 07:14:12 2016-09-18 04:41:40 2016-09-17 16:41:41  163648.0
# 2  2016-09-18 06:16:33 2016-09-18 10:11:43 2016-09-18 10:11:43   14110.0
# 3  2016-09-18 10:11:50 2016-09-18 10:23:11 2016-09-18 10:23:11     681.0
# 4  2016-09-18 10:23:38 2016-09-18 10:30:53 2016-09-18 10:30:54     435.0
# 5  2016-09-18 10:44:18 2016-09-18 10:51:40 2016-09-18 10:51:40     442.0
# =============================================================================

# Task 2 - calculate average distance and duration across taxi types
print(df.groupby('vendor_id')[['dist_meters', 'duration']].mean())
# =============================================================================
#                         dist_meters      duration
# vendor_id                                         
# México DF Radio Taxi     8589.648591   9492.877193
# México DF Taxi Libre     5282.723967   4631.692699
# México DF Taxi de Sitio  7520.609043   8785.155952
# México DF UberBlack      4571.310345   7855.793103
# México DF UberSUV        9381.600000  11031.577778
# México DF UberX          6373.183267   9087.952191
# México DF UberXL         9823.492754  10261.057971
# =============================================================================
print(df.groupby('vendor_id')[['dist_meters', 'duration']].mean().agg({'dist_meters': avg_m, 'duration': avg_dur}))
# =============================================================================
#                       dist_meters        duration
# vendor_id                                          
# México DF Radio Taxi        8.59 km 0 days 02:38:13
# México DF Taxi Libre        5.28 km 0 days 01:17:12
# México DF Taxi de Sitio     7.52 km 0 days 02:26:25
# México DF UberBlack         4.57 km 0 days 02:10:56
# México DF UberSUV           9.38 km 0 days 03:03:52
# México DF UberX             6.37 km 0 days 02:31:28
# México DF UberXL            9.82 km 0 days 02:51:01
# =============================================================================


# Challenge : Corrected Metrics
# =============================================================================
# Average trip duration across different taxi types looks a bit strange. 
# Every taxi type has an average trip duration greater than 1 hour (most of them even greater than 2 hours), 
# while the average distance is less than 10 km. That's extremely slow!
# =============================================================================

# Loading dataset, creating duration column
url = 'https://drive.google.com/uc?id=1pQCA5C4Yvm86rjUIneefI31LNfoywtrU'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated'])
df["duration"] = pd.to_timedelta(df["duration"])

# Defining functions and converting columns
avg_m = lambda x: str(round(x/1000, 2)) + ' km'
avg_dur = lambda x: pd.to_timedelta(round(x, 0), unit = "S")
df['duration'] = df['duration'].map(lambda x: x.total_seconds())

# Task 1 - calculate proportion of long trips (hours >= 3)
## Duration is within total seconds () take floor division of one hour's amount (3600) and see if greater than or equal to 3
three_more_dur = df[df['duration'] // 3600 >=3]
print(three_more_dur['duration'].head(3), '\n', three_more_dur['duration'].head(3).agg({'duration':avg_dur}))
# =============================================================================
# 0     163648.0
# 1      14110.0
# 10     81900.0
# Name: duration, dtype: float64 
#  duration  0    1 days 21:27:28
#           1    0 days 03:55:10
#           10   0 days 22:45:00
# Name: duration, dtype: timedelta64[ns]
# =============================================================================
prop = round(len(three_more_dur)/len(df) * 100, 2)
print(f"There are {prop}% observations having trip duration greater-equal than 3 hours.")
## There are 7.84% observations having trip duration greater-equal than 3 hours.

# Task 2 - calculate the average stats for filtered dataset = take duration under 3 hours (inverse of above more or less)
print(df[df['duration'] // 3600 < 3].groupby('vendor_id').mean().agg({'dist_meters': avg_m, 'duration': avg_dur}))
# =============================================================================
#                         dist_meters        duration
# vendor_id                                          
# México DF Radio Taxi        7.63 km 0 days 00:35:31
# México DF Taxi Libre        4.86 km 0 days 00:20:16
# México DF Taxi de Sitio     6.78 km 0 days 00:27:27
# México DF UberBlack          3.8 km 0 days 00:20:51
# México DF UberSUV           7.61 km 0 days 00:26:45
# México DF UberX              5.3 km 0 days 00:26:22
# México DF UberXL            9.73 km 0 days 00:31:49
# =============================================================================


# Challenge : Group By Period??
# =============================================================================
# So we generally group by a column or hierarchical column grouping but can we do it with some time-series data? 
# For example, can we summarize data by each week presented in dataset? 
# =============================================================================
# =============================================================================
# There is .resample function available to group by different periods from pandas.
# df.resample(rule, axis = 0, closed = None, label = None, convention = 'start', kind = None, loffset = None, 
#   base = None, on = None, level = None, origin = 'start_day', offset = None)

# The most important and the only one required argument is rule - the offset string or object representing target conversion. 
# Easier, it's the period we want to divide our data by.
# =============================================================================
# =============================================================================
# Alias	Meaning
# B	: Business day frequency
# C	: Custom business day frequency
# D	: Calendar day frequency
# W	: Weekly frequency
# M	: Month end frequency
# Q	: Quarter end frequency
# =============================================================================

url = 'https://drive.google.com/uc?id=1pQCA5C4Yvm86rjUIneefI31LNfoywtrU'
df = pd.read_csv(url, parse_dates = ['pickup_datetime', 'dropoff_datetime', 'dropoff_calculated'])
df["duration"] = pd.to_timedelta(df["duration"])
df = df.iloc[:, 3:]
df_gp = df.copy()
print(df_gp.info())
# Task 1 - set pickup_datetime as index for dataframe (simply setting a dataframe's index with a datetime column will produce the same result and type index)
df = df.set_index(pd.DatetimeIndex(df['pickup_datetime']))
df_gp = df_gp.set_index(df['pickup_datetime'])
print(df.index, '\n', df_gp.index)
# Truncating output of each set dataframe index
# =============================================================================
# DatetimeIndex(['2016-09-16 07:14:12', '2016-09-18 06:16:33',
#                ...
#                '2016-10-28 06:49:41', '2016-10-27 10:26:38'],
#               dtype='datetime64[ns]', name='pickup_datetime', length=12402, freq=None) 
#  DatetimeIndex(['2016-09-16 07:14:12', '2016-09-18 06:16:33',
#                ...
#                '2016-10-28 06:49:41', '2016-10-27 10:26:38'],
#               dtype='datetime64[ns]', name='pickup_datetime', length=12402, freq=None)
# =============================================================================

# Task 2 - calculate number of trips in each month available in dataset
print(df.resample('M').size().sum(), len(df))
# Take the count of seen rows for each month
print(df.resample('M').size(),type(df.resample('M').size()))
# =============================================================================
# pickup_datetime
# 2016-06-30      77
# 2016-07-31     283
# 2016-08-31     614
# 2016-09-30     538
# 2016-10-31     891
# 2016-11-30    1075
# 2016-12-31    1081
# 2017-01-31    1105
# 2017-02-28     644
# 2017-03-31     952
# 2017-04-30    1002
# 2017-05-31    1114
# 2017-06-30    1829
# 2017-07-31    1197
# Freq: M, dtype: int64
# =============================================================================
## Type DatetimeIndex Filtering with .loc[] 
print(df.loc[(df.index >= '2016-06-01') & (df.pickup_datetime < '2016-07-01')])
# =============================================================================
#                        id  ...  dropoff_calculated
# pickup_datetime            ...                    
# 2016-06-27 09:25:42  4653  ... 2016-06-27 09:49:46
# 2016-06-26 04:32:53  4654  ... 2016-06-26 04:47:40
# 2016-06-27 02:13:35  4655  ... 2016-06-27 02:15:26
# 2016-06-27 12:54:57  4656  ... 2016-06-27 13:12:53
# 2016-06-27 02:03:22  4657  ... 2016-06-27 02:20:58
#                   ...  ...                 ...
# 2016-06-30 02:00:48  8337  ... 2016-06-30 02:05:32
# 2016-06-29 03:28:24  8338  ... 2016-06-30 16:08:18
# 2016-06-30 04:08:22  8339  ... 2016-06-30 05:15:36
# 2016-06-30 05:34:58  8340  ... 2016-06-30 05:43:10
# 2016-06-30 09:10:06  8341  ... 2016-06-30 09:11:16
# 
# [77 rows x 14 columns]
# =============================================================================
df_gp_sorted = df_gp.sort_index(ascending=True)
print(len(df_gp_sorted) == len(df))
## True
print(df_gp_sorted.iloc[:80, :2])
# Note here below that from row 75:80 (last 5 rows) we can clearly see a new month on the 3rd to last line 
# indicating the  accuracy of 77 provided by the .resample method above with the chained size call 
# =============================================================================
#                        id                vendor_id
# pickup_datetime                                   
# 2016-06-24 08:37:31  5229     México DF Radio Taxi
# 2016-06-24 11:05:38  5230  México DF Taxi de Sitio
# 2016-06-24 11:07:34  5232  México DF Taxi de Sitio
# 2016-06-24 11:07:34  5231  México DF Taxi de Sitio
# 2016-06-25 01:28:58  5234     México DF Taxi Libre
#                   ...                      ...
# 2016-06-30 11:06:36  8335  México DF Taxi de Sitio
# 2016-06-30 11:23:57  8336     México DF Taxi Libre
# 2016-07-01 06:56:54  8342     México DF Taxi Libre
# 2016-07-01 09:36:57  8343  México DF Taxi de Sitio
# 2016-07-01 11:20:43  8344  México DF Taxi de Sitio
# =============================================================================
# df.index.to_series().between('2018-01-01', '2018-01-10') - Filter datetime index between(inclusive date value, exclusive date value)
june_16 = df_gp.loc[df_gp.index.to_series().between('2016-06-01', '2016-07-01')]
print(len(june_16))
## 77
# Get first and last row to confirm final month entries in above table read out after sorting subset june dataframe rows
print(june_16.sort_index().iloc[[0, -1], :2])
# =============================================================================
#                        id             vendor_id
# pickup_datetime                                
# 2016-06-24 08:37:31  5229  México DF Radio Taxi
# 2016-06-30 11:23:57  8336  México DF Taxi Libre
# =============================================================================


