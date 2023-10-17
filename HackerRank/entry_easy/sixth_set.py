#### **Date and Time - Calendar Module** ####
# Calendar Module
# The calendar module allows you to output calendars and provides additional useful functions for them.

# class calendar.TextCalendar([firstweekday])

# This class can be used to generate plain text calendars.

# Input Format

# A single line of input containing the space separated month, day and year,
# respectively, in "MM DD YYYY" format.

# Sample Input

# 08 05 2015

# Sample Output

# WEDNESDAY


## Code and solving
# Quick printout here of how we got the values and the weekday int value 

import calendar
date_values = list(map(int, input().split()))
print([(x, type(x)) for x in date_values], len(date_values))
month, day, year = date_values
cal_weekday_int = calendar.weekday(year, month, day)
print(month, day, year, cal_weekday_int, sep='\n')


# https://stackoverflow.com/questions/37852884/python-converting-a-day-number-to-a-day-name-using-calendar
import calendar
date_values = list(map(int, input().split()))
month, day, year = date_values
cal_weekday_int = calendar.weekday(year, month, day)
print(calendar.day_name[cal_weekday_int].upper())


#### **Errors and Exceptions** ####
# Task

# You are given two values a and b.
# Perform integer division and print a/b.

# Input Format

# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.

# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = int(input())
for i in range(cases):
    try:
        a, b = input().split()
        print(int(int(a) / int(b)))
    except ValueError as e:
        print('Error Code:', e)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')

# Input
# 3
# 1 0
# 2 $
# 3 1

# Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3


#### ** Errors And Execption - Incorrect Regex** #### 
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format

# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')

# Input
# 2
# .*\+
# .*+

# Output
# True
# False

