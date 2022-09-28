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

from datetime import date

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

# Update yesteday/future values with today date object : set default

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
print(deft[0][1], type(deft[0][1]))
print(type(deft[0]), type(deft[1]))
for rtrn in deft:
    for tup in rtrn:
        print(tup)
# Quick pull for each tuple type to confirm function return and class type (json_str) (json_dict)
print([(type(x[0]), type(x[1])) for x in deft])
# Strings passed to json load
print([(x[0], type(x[0])) for x in deft])
# JSON Dictinaries
print([(x[1], type(x[1])) for x in deft])








