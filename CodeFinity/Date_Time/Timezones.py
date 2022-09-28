#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:41:34 2022

@author: craigrupp
"""

# The Variery of Timezones - pytz library
# =============================================================================
# In two previous sections, we worked with dates and times, without taking into account the timezone. 
# While planning the meeting with foreigners, planning to fly to another country, 
# or planning to watch some sporting event, you have to take this into account.
# 
# to handle timezones, we will use pytz library, which brings the tz database (also known as Olson database) in Python. 
# =============================================================================

# =============================================================================
# Let's start with the exploration of available timezones. 
# There are two methods available in pytz: .all_timezones will return a list with all the available timezones in pytz, 
# and .common_timezones will return only the common ones.
# =============================================================================
# Load library
import pytz


# Find the number of timezones - note here is these look like variables/properties : unsure of why declared as methods above from content
print(f"Number of available timezones: {len(pytz.all_timezones)}")
## Number of available timezones: 594
print(f"Number of common timezones: {len(pytz.common_timezones)}")
## Number of common timezones: 439

# Print the 100-th common timezone
print(f"100-th common timezone: {pytz.common_timezones[99]}")
## 100-th common timezone: America/Edmonton


# More Timezone Examples : Iterability of Timezones from property returns above
# =============================================================================
# In the previous chapter, you saw one timezone: America/Edmonton. 
# But the total number of even common timezones is quite big: more than 400! 
# But you can see, that timezone by default contain continent name and city. 
# So, we can explore the variety of timezones across the specific continent.
# List type returns from methods/props above allow for ways to filter through all timezones easier
# =============================================================================

# Count number of american timezones using list comprehension
american_timezones = len([x for x in pytz.common_timezones if 'America' in x])
print(f"There are {american_timezones} american timezones available in pytz.common_timesones.")
## There are 147 american timezones available in pytz.common_timesones.

eur_timezones = []
# Iterate over .common_timezones
for i in pytz.common_timezones : 
  # Check if string contains 'Europe'
  if 'Europe' in i: 
    # If yes, print its name
    eur_timezones.append(i) 
    
print(len(eur_timezones))
## 60

# Let's look at 10
print(eur_timezones[:10])
## ['Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest']



## Applying Timezone to Datetime Object - Label Timezone & Convert Existing Datetime Object

# Label Timezone
# =============================================================================
# Now we know about the variety of available timezones.
# How can we adjust it to a certain datetime object? 
# How to make Python diff two datetime objects with different locations?
# =============================================================================
# =============================================================================
# The algorithm is: create datetime object and save timezone within it using .localize() method. 
# To do it, we will need to load timezone from pytz library. Then, we will need to create a timezone object, 
# and then apply .localize() function to datetime object.
# =============================================================================

from pytz import timezone
from datetime import datetime

tz = timezone('Europe/Warsaw') # save timezone
dt = datetime(2021, 11, 1, 11, 25, 0) # create datetime object

# Apply timezone to dt
dt_tz = tz.localize(dt)
print(f"Datetime object with timezone: {dt_tz}")
## Datetime object with timezone: 2021-11-01 11:25:00+01:00


# GMT is 4 hours ahead of New York - Let's set a 

# Task 1: Set timezone for New York
tz = timezone('America/New_York')

# Task 2: create datetime object
now = datetime.now()

# Task 3: apply tz timezone to now datetime object
now_tz = tz.localize(now)

# Printing and comparing the results
print(f"Current timestamp: {now}")
## Current timestamp: 2022-09-28 15:59:04.135285
print(f"Current timestamp with timezone: {now_tz}")
## Current timestamp with timezone: 2022-09-28 15:59:04.135285-04:00


# What Time is it in ... ? - Convert Existing Datetime Object
# =============================================================================
# The previous method simply labels to datetime timezone. 
# The second approach is to convert existing datetime objects with no timezone to a certain timezone.
# Apply .astimezone() method to datetime object with timezone object as an argument.
# =============================================================================

tz_mu = timezone('Europe/Warsaw') # save timezone
dt_mu = datetime(2021, 11, 1, 11, 25, 0) # create datetime object

dt_tz_mu = dt.astimezone(tz_mu) # convert dt to tz timezone

# Testing
print(f"Saved time: {dt_mu}")
print(f"Converted time: {dt_tz_mu}")

now_az = datetime.now()
print(now_az)
## 2022-09-28 16:11:20.312340

now_az = now_az.astimezone(timezone('America/New_York'))
print(now_az)
## 2022-09-28 17:11:20.312340-04:00



## Daylight Savings Time
# =============================================================================
# To take into consideration possible DST shift use .normalize method on timezone object with timedelta object with timezone set as an argument. 
# For example, in 2021 Ukraine set its clocks forward by one hour on 28 March at 03:00 (local time). 
# So, it should be impossible to have 03:30 time on this date (since 03:00 became 04:00). 
# =============================================================================
tz = timezone('Europe/Kiev') # timezone object
dt = datetime(2021, 3, 28, 3, 35) # datetime object

# Set timezone to datetime 
dt_tz = tz.localize(dt)

dt_tz_norm = tz.normalize(dt_tz) # adjust time to DST

# Testing - Offset for normalized timezone visible below 
print(f"Original datetime: {dt_tz}")
## Original datetime: 2021-03-28 03:35:00+02:00
print(f"Normalized datetime: {dt_tz_norm}")
## Normalized datetime: 2021-03-28 04:35:00+03:00


# =============================================================================
# There is only one correct answer when we are talking about the 'spring forward' shift. 
# But if we are talking about 'fall back' shift there is no correct answer, since one time happens twice. 
# For example, in 2021 Ukraine set its clocks back by one hour on 31 October at 04:00 (local time). 
# So, there was, for example, 03:30 happened twice (before and after setting clocks).
# =============================================================================
# Datetime objects
dt1 = datetime(2021, 3, 13, 2, 30)
dt2 = datetime(2021, 3, 14, 2, 30)
dt3 = datetime(2021, 3, 14, 3, 30)

# Timezone object
tz_la = timezone('America/Los_Angeles')

# Setting timezone to datetime objects
dt_tz1 = tz_la.localize(dt1)
dt_tz2 = tz_la.localize(dt2)
dt_tz3 = tz_la.localize(dt3)

# Adjust possible DST shift
dt1_norm = tz.normalize(dt_tz1)
dt2_norm = tz.normalize(dt_tz2)
dt3_norm = tz.normalize(dt_tz3)

# Testing
print(f"Original date 1: {dt_tz1}; Normalized: {dt1_norm}")
print(f"Original date 2: {dt_tz2}; Normalized: {dt2_norm}")
print(f"Original date 3: {dt_tz3}; Normalized: {dt3_norm}")

# =============================================================================
# Original date 1: 2021-03-13 02:30:00-08:00; Normalized: 2021-03-13 12:30:00+02:00
# Original date 2: 2021-03-14 02:30:00-08:00; Normalized: 2021-03-14 12:30:00+02:00
# Original date 3: 2021-03-14 03:30:00-07:00; Normalized: 2021-03-14 12:30:00+02:00
# =============================================================================
















