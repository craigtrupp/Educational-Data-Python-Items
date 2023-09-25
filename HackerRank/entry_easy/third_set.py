#### **Strings - Designer Door Mat** #### 
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

## Sample Design
# Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
import statistics as stats
catch = input()
items = [int(x) for x in catch.split()] # transform n, m to int for operations down the line
n, m = items[0], items[1]
surrounding_pattern = '.|.'
offset = 1
# use stats library to get median of N (N = 7, median needs = list of all integers up to N)
break_point = stats.median([x for x in range(1, n + 1)]) # [for n = 7 [1,2,3,4,5,6,7]]
string_rows = []
for i in range(1, n + 1):
    if i < break_point:
        string_rows.append((surrounding_pattern * offset).center(m, '-'))
        offset += 2
    elif i == break_point:
        string_rows.append('WELCOME'.center(m, '-'))
    else:
        offset -= 2
        string_rows.append((surrounding_pattern * offset).center(m, '-'))
print( '''{}'''.format('\n'.join(string_rows)))



#### **Strings - Formatting i to N Types** ####
# Given an integer, n, print the following values for each integer i from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# * int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above 
# for each i from 1 to number. Each value should be space-padded to match the width of the binary value 
# of number and the values should be separated by a single space.

# Input Format

# A single integer denoting n.
def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1, n + 1):
        decimal = i
        octal = oct(i).lstrip('0o')
        hexadecimal = hex(i).lstrip('0x').upper()
        binary = bin(i).lstrip('0b')
        print(str(decimal).rjust(width),str(octal).rjust(width),
        str(hexadecimal).rjust(width),str(binary).rjust(width))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



#### **Strings - Alphabet Rangoli** #### 
# You are given an integer, n. Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:
# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

### Just a little terminal session for string formatting
# >>> print(len('--------e--------'))
# 17
# >>> print(len('--------'))
# 8
# >>> print(len('----c----'))
# 9
# >>> print(len('c-b-a-b-c'))
# 9
# >>> print(len('e-d-c-b-a-b-c-d-e'))
# 17
# >>> print('e-d-c-b-a-b-c-d-e'.center(17, '-'))
# e-d-c-b-a-b-c-d-e

### Second part after getting all string characters for first part
# >>> s
# 'aabbccdd'
# >>> [s[i:i+1] for i in range(0, len(s))] # essentially here we're just taking the string, and indexing at each location through the loop
# ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'] # now with a list we can use a character to join with
# >>> '-'.join([s[i:i+1] for i in range(0, len(s))])
# 'a-a-b-b-c-c-d-d'

from string import ascii_lowercase

def print_rangoli(size): # input value is 5 here so e in the dictionary when offset accounted for
    # your code goes here
    alpha_dict = {v:k for k,v in enumerate(ascii_lowercase)}
    # print(alpha_dict) # {'a': 0, 'b': 1} ... and so on (https://stackoverflow.com/questions/63915659/ create-dictionary-with-alphabet-characters-mapping-to-numbers)
    # alright so no we want to see what our offset our maximum string is for center with m 
    strings = []
    for i in range(1, size + 1):
        str_row_chars = '' # default empty string to add representing a row
        for l in range(0, i):
            size_offset = size - 1 # to locate in dictionary more easily (recall we're getting the key and not the value so different indexing approach)
            str_row_chars += [k for k, v in alpha_dict.items() if v == size_offset - l][0] # only ever one value so can just grab
        print(str_row_chars)
        strings.append(str_row_chars)
    print(strings) # with 5 as input this returns : ['e', 'ed', 'edc', 'edcb', 'edcba']
            
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

## print statement from outer look of print(str_row_chars)
# e
# ed
# edc
# edcb
# edcba

## So now that we have the strings for our rows, we need to add the padding in between (see below for that stage)
from string import ascii_lowercase

def print_rangoli(size):
    # your code goes here
    alpha_dict = {v:k for k,v in enumerate(ascii_lowercase)}
    # print(alpha_dict) # {'a': 0, 'b': 1} ... and so on (https://stackoverflow.com/questions/63915659/ create-dictionary-with-alphabet-characters-mapping-to-numbers)
    # Below Nested loop iterates for the amount of rows to center and dynamically gets the "left part of alpha for each row (see strings-print)"
    strings = []
    for i in range(1, size + 1):
        str_row_chars = '' # default empty string to add representing a row
        for l in range(0, i):
            size_offset = size - 1 # to locate in dictionary more easily (recall we're getting the key and not the value so different indexing approach)
            str_row_chars += [k for k, v in alpha_dict.items() if v == size_offset - l][0] # only ever one value so can just grab
        strings.append(str_row_chars)
    print(strings) # with 5 as input this returns : ['e', 'ed', 'edc', 'edcb', 'edcba']
    # So now we need to the dash in between the strings with a len greater > 1  
    for idx, string in enumerate(strings):
        #print(string, idx)
        if idx > 0:
            char_list = [x for x in string] # ['e', 'ed'] ex
            strings[idx] = '-'.join(char_list)
    print(strings) # after mutating strings for character in between : ['e', 'e-d', 'e-d-c', 'e-d-c-b', 'e-d-c-b-a']

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)