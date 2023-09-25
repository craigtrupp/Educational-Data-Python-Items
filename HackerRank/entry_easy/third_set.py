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
