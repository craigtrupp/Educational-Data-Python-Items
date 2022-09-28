#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:36:21 2022

@author: craigrupp
"""
# Course Intro
# =============================================================================
# Dates and(or) times are one of the most common things in modern data: often we need to deal with observations containing dates and times. 
# In this course, you will learn about datetime, pytz libraries, and how they help to deal with different formats of dates and times. 
# Also, you will learn how to implement this knowledge to work with dirty or missing date/time values.
# =============================================================================

## Since we are going to work with only dates, we will import only date class from the datetime library.

from datetime import date, timedelta

today = date.today()
print(today)

# =============================================================================
# # Create Custome Date Object 
# Please note, that there are 3 and only 3 required arguments. 
# Please note, that zero-padded numbers are not allowed as arguments. 
# You can use either positional or keyword arguments : position
# # Date(year, month, day)
# =============================================================================
yesterday = date(day=27, month=9, year=2022)
# Positionally
future = date(2022,9,29)
print([(x, type(x)) for x in [yesterday, future]])


# Attributes
# =============================================================================
# Since date is an object, it should have some attributes. Let's consider them:
# 
# date.day - extracts day of the month (between 1 and number of days in the given month of the given year);
# date.month - extracts month of the year;
# date.year - extracts year of the given date;
# =============================================================================
# Using datetime object variable above

print(f"Today's date attributes are : 'day' : {today.day}, 'month' : {today.month}, 'year': {today.year}")


# Date Methods
# =============================================================================
# There are also several methods available for date objects. Let's consider some of them:
# 
# date.weekday() - returns the day of week as an integer (0 is Monday, 6 is Sunday);
# date.isoweekday() - returns the day of week as an integer (but this time 1 for Monday, and 7 for Sunday);
# date.replace(year = ..., month = ..., day = ...) - replaces the specified arguments for given date object.
# =============================================================================
print(f"Today's weekday as a zero index : {today.weekday()} which is a ", today.strftime("%A"))
print(f"Todays weekday starting as a 1 index : {today.isoweekday()}, which is a : {today.strftime('%A')}")
print(today.replace(2018, 4, 18), type(today.replace(2018, 4, 18)))
# return's new string, doesn't mutate date object in place
print(today)

# Create date object
halloween = date(2021, 10, 31)

# Find the day of week of halloween
print(halloween.weekday())

# Create variable halloween_next with 2022 year
halloween_next = halloween.replace(year = 2022)

# Find out day of week for halloween_next
print(halloween_next.weekday())



def yesterday_tomorrow(day=date.today()):
    """
    Parameters
    ----------
    day : datetime.date object
        Default argument will use today's date but a custom date object can be passed as well.

    Returns
    -------
    Python List :
        JSON string and object in tuple position [0, 1] for returned list with two tuple objects
        [(ystr.dumps, ystr.loads), (tmr.dumps, tmr.loads)]
    """
    # Load in required libraries
    from datetime import timedelta
    import json
    # Create new date objects
    yesterday = day - timedelta(days=1)
    tomorrow = day + timedelta(days=1)
    # Generate string format to return with date objects dictionary
    ystr_day, ystr_month, ystr_year = yesterday.strftime("%A"), yesterday.strftime("%b"), yesterday.strftime("%Y")
    ystr_json_str = json.dumps({'yesterday_date': {'day':yesterday.day, 'month':yesterday.month, 'year':yesterday.year}, 
                      'yesterday_string' : f"Yesterday was {ystr_month}, {yesterday.day} {ystr_year}. This was a {ystr_day}"})
    tmr_day, tmr_month, tmr_year = tomorrow.strftime("%A"), tomorrow.strftime("%b"), tomorrow.strftime("%Y")
    tmr_json_str = json.dumps({'tomorrow_date': {'day':tomorrow.day, 'month':tomorrow.month, 'year':tomorrow.year}, 
                      'tomorrow_string' : f"Tomorrow is {tmr_month}, {yesterday.day} {tmr_year}. This was a {tmr_day}"})
    return [(ystr_json_str, json.loads(ystr_json_str)), (tmr_json_str, json.loads(tmr_json_str))]
    

deft = yesterday_tomorrow()
# Date must have occurred in order for logic to work (maybe a time delta thing)
halloween = date(2022, 10, 31).replace(year=2021)
print(yesterday_tomorrow(halloween))
print(deft[0][1], type(deft[0][1]))
print(type(deft[0]), type(deft[1]))
for rtrn in deft:
    for tup in rtrn:
        print(tup)
# Quick pull for each tuple type to confirm function return and class type (json_str) (json_dict)
print([(type(x[0]), type(x[1])) for x in deft])
# Strings passed to json load
print([(x[0], type(x[0])) for x in deft])
# =============================================================================
# [('{"yesterday_date": {"day": 27, "month": 9, "year": 2022}, "yesterday_string": "Yesterday was Sep, 27 2022. This was a Tuesday"}', <class 'str'>),
# ('{"tomorrow_date": {"day": 29, "month": 9, "year": 2022}, "tomorrow_string": "Tomorrow is Sep, 27 2022. This was a Thursday"}', <class 'str'>)]
# =============================================================================
# JSON Dictinaries
print([(x[1], type(x[1])) for x in deft])
# =============================================================================
# [({'yesterday_date': {'day': 27, 'month': 9, 'year': 2022}, 'yesterday_string': 'Yesterday was Sep, 27 2022. This was a Tuesday'}, <class 'dict'>), 
#  ({'tomorrow_date': {'day': 29, 'month': 9, 'year': 2022}, 'tomorrow_string': 'Tomorrow is Sep, 27 2022. This was a Thursday'}, <class 'dict'>)]
# =============================================================================



# Date Formats
# =============================================================================
# So, how can we transform the date object into another format? 
# At first, we need to load datetime class from the datetime library within a new line (yes, sounds tautological). 
# Then, you need to apply .strftime() method of datetime class (datetime.strftime()) with a date as the first argument, and pattern as the second.
# https://www.programiz.com/python-programming/datetime/strftime
# =============================================================================

## See above for usage within the yestrday_tomorrow function as well

# Create date object
day = date(1998, 3, 11)

# Format date into another format
day_formatted = day.strftime("%d.%m.%y")
print("Original date:", day)
print("Formatted date:", day_formatted)


# Format date into another format
day_formatted_deux = day.strftime("%A, %d of %B, %Y")
print("Original date:", day)
print("Formatted date:", day_formatted_deux)



# Date Difference
# =============================================================================
# There is timedelta class in the datetime library, which object represents a duration, the difference between two dates or times. 
# timedelta object has 7 arguments, all optional (days, seconds, microseconds, milliseconds, minutes, hours, weeks). 
# Since we are working with dates only, we will focus on only days argument. 
# Note, that argument weeks converts into 7 days. By default, the difference between two dates/times will be represented as the number of days, hours, minutes, and seconds. 
# Since we are comparing dates, all the arguments but days will be 0. For example, the WHO declared the COVID-19 pandemic on 11 March 2020. 
# We can count the number of days since this event till today.
# =============================================================================

pandemic = date(2020, 3, 11)
print(today - pandemic, "passed since COVID-19 became pandemic")

## Create two date objects date1 and date2 with dates "14 January 2016" and "07 April 2019" respectively. Find the difference between these two dates.
# Create date objects
date1 = date(2016, 1, 14)
date2 = date(2019, 4, 7)

# Find the difference between date2 and date1
print("The difference between date2 and date1:", date2 - date1)



# Arithmetic Operations with timedelta Objects
# =============================================================================
# For example, we can calculate the whole number of weeks between two dates. 
# Let's use the same example as before: we can calculate the whole number of weeks since the COVID-19 became a pandemic (declared by WHO). 
# There are two ways to solve this task:
# 
# Extract the number of days (by using .days) and then find the whole part of division by 7.
# Find the whole part of the division of two timedelta objects.
# =============================================================================

# Calculate difference between dates
diff = today - pandemic
# Default the days, hours:minutes:seconds detailed above
print(diff) 
# Count whole number of weeks: method 1 (Floor division so as to count)
print(diff.days//7, "weeks passed since COVID-19 became pandemic")
print(diff.days/7, " weeks since COVID-19 became pandemic")

# Count whole number of weeks: method 2
print(diff//timedelta(weeks = 1), "weeks passed since COVID-19 became pandemic")

937/7
(932/7)
# Get decimal percent to 1 to get total days
(100/7)/100
6/7
# Function to Get days if diff maintains a remainder

def get_weeks_days_difference(dt=date(2022,1,1)):
    """
    Logic
    ---------
    Use timedelta objects and modulus return to return amount of time passed in days/weeks
    
    Parameters
    ----------
    dt : datetime object, optional
        Datetime (Ideally in the past) passed to function to get duration of weeks/days since dates. The default is date.today().

    Returns
    -------
    difference in time duration in weeks, days || days if difference in time delta diff is less than 1 week

    """
    from datetime import date as d_today
    diff = d_today.today() - dt
    print(type(diff))
    # diff defaults is "{# of } days, 0:00:00"
    # Use timedelta diff objects days property and capture weeks passed with no remainder (at least 1 week)
    # Value Error if timedelta not >= 1
    if diff.days <= 0:
        raise ValueError('Argument provided to find difference in duration is not prior to Today')
    else:
        if diff.days % 7 == 0 and diff.days >= 7:
            return f"A total of {int(diff.days / 7)} week(s) has passed"
        # Similarly use property but grab week and days since event passed with default of at least 8 days in difference
        elif diff.days % 7 != 0 and diff.days >= 8:
            return f"A total of {diff.days // 7} week(s) and {diff.days%7} day(s) have passed"
        # Get Days difference that is less than a week and more than one day
        else:
            return f"A total of {diff.days} day(s) have passed"
    

valerr = get_weeks_days_difference(today)
print(valerr)
# ValueError: Argument provided to find difference in duration is not prior to Today

two_weeks = get_weeks_days_difference(date(2022,9,14))
print(two_weeks)
# A total of 2 week(s) has passed

ten_days = get_weeks_days_difference(date(2022,9,18))
print(ten_days)
# A total of 1 week(s) and 3 day(s) have passed

five_days = get_weeks_days_difference(date(2022,9,23))
print(five_days)
# A total of 5 day(s) have passed

# Time delta object
# print(eight_days[0].__dict__.keys())
# print(eight_days[0].__dict__.values())

## Quick Exercise on the platform
from datetime import timedelta
# Create two date objects
date1 = date(2016, 1, 14)
date2 = date(2019, 4, 7)

# Calculate difference between dates
date_diff = date2 - date1

# Use .days method
print("There were", date_diff.days//7, "weeks between date1 and date2.")

# Use timedelta
print("There were", date_diff//timedelta(weeks=1), "weeks between date1 and date2.")
