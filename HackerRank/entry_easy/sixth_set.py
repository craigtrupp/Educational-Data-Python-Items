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




#### **itertools.combinatinos** ####
# itertools.combinations(iterable, r)
# This tool returns the r length subsequences of elements from the input iterable.

# Combinations are emitted in lexicographic sorted order. 
# So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

# >>> from itertools import combinations
# >>> 
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>> 
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string 
# in lexicographic sorted order

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Output Format
# Print the different combinations of string S on separate lines.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string, diff_combinations = input().split()
diff_combinations = int(diff_combinations)
total_combinations = list([combinations(string, i) for i in range(1, diff_combinations + 1)])
print(total_combinations)
for itertool_x in total_combinations:
    iter_list = list(itertool_x)
    print(iter_list)

# First round of outputs  - Now need to sorted lexically and print out each item
# [<itertools.combinations object at 0x7f0ab28b8720>, <itertools.combinations object at 0x7f0ab28b8b80>]
# [('H',), ('A',), ('C',), ('K',)]
# [('H', 'A'), ('H', 'C'), ('H', 'K'), ('A', 'C'), ('A', 'K'), ('C', 'K')]

## ... We're gonna try and have a little fun with a sorting algo here
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
# string, diff_combinations = input().split() - for my fun
string, diff_combinations = 'HACK', 3
diff_combinations = int(diff_combinations) 
total_combinations = list([combinations(string, i) for i in range(1, diff_combinations + 1)])
combo_pairs_sorting = []
# so we can look at maybe sorting the combinations longer than 1
# only the combination of values (not their position) is unique so we shouldn't have any duplicates
for combos in total_combinations:
    # Here we can see if the length of the combos is greater than 1 and then use sorting logic
    combo_list = list(combos)
    len_check = all([True if len(i) == 1 else False for i in combo_list])
    if len_check is True:
        combo_pairs_sorting.append(sorted(combo_list))
    else: 
        # ... we're gonna try to get a bit crazy and sort ourselves
        print(combo_list)
        mutated_combo_list = [list(x) for x in combo_list]
        ordered_pair_sets = []
        for list_tup in mutated_combo_list:
            for idx in range(len(list_tup) - 1):
                if list_tup[idx] > list_tup[idx + 1]:
                    tmp = list_tup[idx]
                    list_tup[idx] = list_tup[idx + 1]
                    list_tup[idx + 1] = tmp
            ordered_pair_sets.append(tuple(list_tup))
        print(ordered_pair_sets)
        break
         
print(combo_pairs_sorting)
    
# Here's the Output - Got have a temp to store current value in sorting logic before changing
# [('H', 'A'), ('H', 'C'), ('H', 'K'), ('A', 'C'), ('A', 'K'), ('C', 'K')]
# [('A', 'H'), ('C', 'H'), ('H', 'K'), ('A', 'C'), ('A', 'K'), ('C', 'K')]
# [[('A',), ('C',), ('H',), ('K',)]]