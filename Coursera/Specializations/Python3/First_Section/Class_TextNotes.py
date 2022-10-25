#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:05:56 2022

@author: craigrupp
"""
## Str Type combinations
# =============================================================================
# Double quoted strings can contain single quotes inside them, as in "Bruce's beard", and single quoted strings can have double quotes inside them, 
# as in 'The knights who say "Ni!"'. Strings enclosed with three occurrences of either quote symbol are called triple quoted strings. T
# hey can contain either single or double quotes:
# =============================================================================
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') # "Oh no", she exclaimed, "Ben's bike is broken!"

      
## Good Reminder that variable reassignment doesn't follow after assignment
a = 5
b = a    # after executing this line, a and b are now equal
print(a,b)
a = 3    # after executing this line, a and b are no longer equal
print(a,b)

# 5 5
# 3 5
print(a ==  b) # False


## Input
str_seconds = input("Please enter the number of seconds you wish to convert : ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)



## Range Usage for concatenating and dataframe sum usage with sample dataframe with years as such
print(list(range(1980,1990)))


Eighty_80s = [x for x in range(1980,1990)]
Ninety_90s = [x for x in range(1990,2000)]
Millenium = [x for x in range(2000,2014)]

# Initializing lists
test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, 5]
  
# using + operator to concat
test_list5 = test_list3 + test_list4
print(test_list5)


# Using map to update a type from a returned range, then transformed into a list
print(list(range(1980,2014)))
print(list(map(str, range(1980, 2014))))

## Map is Great!
# =============================================================================
# [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
# ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
# 
# =============================================================================

















