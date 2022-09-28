#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:43:28 2022

@author: craigrupp
"""
# Datetime
# =============================================================================
# A datetime object has 6 additional arguments compared to a date object. 
# These are hour (0-24), minute (0-60), second (0-60), microsecond (0-1000000), tzinfo, and fold (used for local times).
# =============================================================================
# Load class from library
from datetime import datetime

# Print current date and time
print("Now it's", datetime.now(), "GMT")
## Now it's 2022-09-28 14:46:36.727098 GMT

# Extend on Datetime object
# =============================================================================
# Positional Argumenst (Hour/Minute/Second)
# =============================================================================

# Create datetime object using keyword arguments
d = datetime(month = 11, year = 2017, day = 17, hour = 12, minute = 34, second = 56)
# Create datetime object using positional arguments
t = datetime(2017, 11, 17, 12, 34, 56)

# Check their values
print("Are", d, "and", t, "equal:", d == t)
## Are 2017-11-17 12:34:56 and 2017-11-17 12:34:56 equal: True
print(type(d), type(t), type(d) == type(t))
## <class 'datetime.datetime'> <class 'datetime.datetime'> True


# Further Datetime Attributes
# =============================================================================
# Like for date objects, there are also attributes for datetime allowing us to extract any part of the date and time we want. These are:
# 
# datetime.year - extracts year;
# datetime.month - extracts month;
# datetime.day - extracts day of the month;
# datetime.hour - extracts hour from time;
# datetime.minute - extracts minute from time;
# datetime.second - extracts second from time;
# datetime.microsecond - extracts microseconds from time.
# =============================================================================
# Create datetime object
dt = datetime(2013, 5, 15, 18, 10, 52)

# Extract day and month
print(f"Day:Month - {dt.day}.{dt.month}")
## Day:Month - 15.5
# Extract hour and minute
print(f"Hour:Minute - {dt.hour}:{dt.minute}")
## Hour:Minute - 18:10



# Datetime Methods
# =============================================================================
# But since we expand date with time there have to be some new methods. 
# For example, we can split datetime objects into date and time objects. 
# In the previous chapter, we used .day, .minute and other methods to extract specific dimensions of a datetime object. 
# These methods are:
# 
# datetime.date() - returns date of datetime object;
# datetime.time() - returns time of datetime object;
# =============================================================================
# Create datetime object
dt_m = datetime(1995, 12, 30, 23, 45, 37)

# Extract day of week
print(dt_m.isoweekday())

# Extract date and time objects
print(f"Date: {dt_m.date()}")
## Date: 1995-12-30
print(f"Time: {dt_m.time()}")
## Time: 23:45:37


# =============================================================================
# # Datetime Formats (Time Included)
# =============================================================================
# Create datetime object
dt_f = datetime(2020, 11, 1, 11, 20, 25)

# Format datetime object to some format
dt_formatted = dt_f.strftime("%H:%M %d.%m.%Y")
print(dt_formatted)
## 11:20 01.11.2020


another_format = datetime(2002, 6, 28, 14, 58, 41)

# Format datetime object
print(f"Formatted datetime object: {another_format.strftime('%m/%d/%y %H:%M')}")
## Formatted datetime object: 06/28/02 14:58




# 12 & 24 Hour Formats
# =============================================================================
# Many countries use the 24-hour format in documents, but 12-hour format in daily communication. 
# At the same time, many countries use the 12-hour time format only. 
# So, we need to learn how to deal with and be able to format such times.
# =============================================================================

# Create datetime object
dt_hr = datetime(2002, 6, 28, 14, 58, 41)

# Format time into 24-hour format
print(f"24-hour format: {dt_hr.strftime('%H:%M')}")
## 24-hour format: 14:58
# Format time into 12-hour format
print(f"12-hour format: {dt_hr.strftime('%I:%M %p')}")
## 12-hour format: 02:58 PM



# Date & Time Difference
# =============================================================================
# For example, imagine that we have both departure and arrival times on the ticket. 
# Using timedelta we can easily calculate the expected duration for this trip.
# 
# Departure: 25 May 2021, 18:20
# Arrive: 26 May 2021, 07:40
# =============================================================================
# Create two datetimes objects
dep = datetime(2021, 5, 25, 18, 20)
arr = datetime(2021, 5, 26, 7, 40)

# Calculate estimated trip duration
print(f"Estimated trip duration: {arr - dep}")


# Create departure datetime object
dep_2 = datetime(2022, 7, 19, 15, 0)

# Create arrival datetime object
arr_2 = datetime(2022, 7, 23, 15, 0)

# Calculate trip duration
print(f"Duration of Railway route 'Sydney - Perth' is {arr_2-dep_2}")


# Reading Date and Time from String - datetime.strptime(date string, pattern)
# =============================================================================
# To convert string s into datetime object you need to use datetime.strptime(s, pattern). 
# This will convert the string into a default datetime object.
# 
# The pattern within the function - is the pattern of string you want to convert into datetime object
## You need to detect all the necessary codes satisfying the string!!! 
# =============================================================================

# Dates strings
d1 = "Monday, November 1, 2021"
d2 = "05/23/19 1:23 PM"

# Convert string into datetime objects
dt1 = datetime.strptime(d1, "%A, %B %d, %Y")
dt2 = datetime.strptime(d2, "%m/%d/%y %I:%M %p")

print(f"String '{d1}' converted to datetime: {dt1}")
print(f"String '{d2}' converted to datetime: {dt2}")










