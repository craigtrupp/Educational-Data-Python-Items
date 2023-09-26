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



## Next Step (String Formatting for creating a mirror image)

# Here is our next step (aka reversing the string then selecting up until the last value )
# >>> txt = 'hello'
# >>> txt[::-1]
# 'olleh'
# >>> txt[::-1][:-1]
# 'olle'
# >>> txt = 'hello'
# >>> txt = txt + txt[::-1][1:]
# >>> txt
# 'hellolleh'
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
    # Now we need to do a little reverse and indexing for the string values to provide that mirror type image at the center
    for idx, val in enumerate(strings):
        if idx > 0:
            strings[idx] = strings[idx] + strings[idx][::-1][1:]
    print(strings)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Output at this stage
# ['e', 'ed', 'edc', 'edcb', 'edcba']
# ['e', 'e-d', 'e-d-c', 'e-d-c-b', 'e-d-c-b-a']
# ['e', 'e-d-e', 'e-d-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-b-a-b-c-d-e']

## Now lastly, we just need to extend our strings list to have the indexes up until the last in the mirror image
## Something like this
# >>> list_1 = ['e', 'e-d-e', 'e-d-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-b-a-b-c-d-e']
# >>> list_1.extend(list_1[::-1][1:])
# >>> list_1
# ['e', 'e-d-e', 'e-d-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-b-a-b-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-d-e', 'e-d-e', 'e']
## extend mutates the list in place
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
    # Now we need to do a little reverse and indexing for the string values to provide that mirror type image at the center
    for idx, val in enumerate(strings):
        if idx > 0:
            strings[idx] = strings[idx] + strings[idx][::-1][1:]
    print(strings)
    strings.extend(strings[::-1][1:]) # should mutate in place (no need for variable re-assignment)
    print(strings)
    # now get the max string length to pad then use the center string function to pad for strings not at max length
    max_string_len = len(max(strings, key=len))
    padded_strings = [x.center(max_string_len, '-') for x in strings]
    print(padded_strings)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

## Output for visual logical path
# ['e', 'ed', 'edc', 'edcb', 'edcba']
# ['e', 'e-d', 'e-d-c', 'e-d-c-b', 'e-d-c-b-a']
# ['e', 'e-d-e', 'e-d-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-b-a-b-c-d-e']
# ['e', 'e-d-e', 'e-d-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-b-a-b-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-d-e', 'e-d-e', 'e']
# ['--------e--------', '------e-d-e------', '----e-d-c-d-e----', '--e-d-c-b-c-d-e--', 'e-d-c-b-a-b-c-d-e', '--e-d-c-b-c-d-e--', '----e-d-c-d-e----', '------e-d-e------', '--------e--------']


## Now to tie it all together
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
    # So now we need to the dash in between the strings with a len greater > 1  
    for idx, string in enumerate(strings):
        #print(string, idx)
        if idx > 0:
            char_list = [x for x in string] # ['e', 'ed'] ex
            strings[idx] = '-'.join(char_list)
    # Now we need to do a little reverse and indexing for the string values to provide that mirror type image at the center
    for idx, val in enumerate(strings):
        if idx > 0:
            strings[idx] = strings[idx] + strings[idx][::-1][1:]
    strings.extend(strings[::-1][1:]) # should mutate in place (no need for variable re-assignment)
    # now get the max string length to pad then use the center string function to pad for strings not at max length
    max_string_len = len(max(strings, key=len))
    padded_strings = [x.center(max_string_len, '-') for x in strings]
    return_str = '''{}'''.format('\n'.join(padded_strings)) # print each line in padded list with a new line
    #return return_str (don't get why they want me to print when they should but alright!)
    print(return_str)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


#### **Strings Capitalize** ####
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.
# * alison heck => Alison Heck
# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name, S.
#!/bin/python3

import os

# Complete the solve function below.
def solve(s):
    # Would "title" any character in string based off of whitespace
    return ' '.join([s.title() for s in s.split()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


### I ... was dumb, a lot of test cases failed, need to use a regular expression for pattern capture


# Test Cases : (Input : Expected Output)
# hello   world  lol : Hello   World  Lol
# 1 w 2 r 3g : 1 W 2 R 3g
# 132 456 Wq  m e : 132 456 Wq  M E
# q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M : Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M
# 1 2 2 3 4 5 6 7 8  9 : 1 2 2 3 4 5 6 7 8  9

# Okay so it looks like essentially we want to keep the giant spaces and capitalize any start of alpha string when preceded with a space
# Complete the solve function below.
def solve(s):
    # (\s+) = will split at non-whitespace characters (maintain string length of received arg)
    str_vals = re.split(r'(\s+)', s) # returns list
    # capitalize if captured value at non-whitespace character is alpha, else maintain value
    str_titled = [x.title() if x[0].isalpha() else x for x in str_vals]
    # Now just join for each group of whitespace, alpha or combo which maintains len of original string
    return ''.join(str_titled)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

