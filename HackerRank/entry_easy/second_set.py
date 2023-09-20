#### **Tuples - Challenge** ####
# Task
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line = input()
second_line = input()
# 1 2 is the second line input as a str with a space
tuple_t = tuple(map(int, second_line.split())) # turn each item in the created list to an int and transform object type to a tuple
#print(tuple_t) - (1, 2)
print(hash(tuple_t))

# Oddly the same tuple for the hash built in function was only passing as pypy3 and not python3
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    #print(integer_list) # (1, 2)
    print(hash(integer_list))


#### **Collections - OrderedDict Challenge** ####
# collections.OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.
## Challenge - Task
# Task

# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

## Ok so the way to get each item is to call input() after getting a first read out of how many items there will be
## so 9 on the first input would indicate you need to iterate through 9 sequence of input to generate the item and count to add to the ordered dict
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
item_count = int(input())
ordered_dictionary = OrderedDict() # object to hold ordered place of addition to dictionary
for x in range(item_count):
    line_item = input()
    price = 0
    item = ''
    # now we can loop through the str containing the item/price (sep by space)
    # and use a try/except to set our values for the price/item before mutating or adding to ordered_dictionary
    for itm in line_item.split():
        try:
            int(itm)
            price = int(itm)
        except ValueError:
            #print(f'{itm} is not a base literal to mutate to an int') BANANA is not a base literal to mutate to an int (sample)
            item += f' {itm}'
    # Need to strip leading space for item - space in above creates for items with more than one word
    item = item.strip()
    # Now we nee to either set the key or append the price to the overall keys value
    if ordered_dictionary.get(item):
        ordered_dictionary[item] += price 
    else:
        ordered_dictionary[item] = price
# Now that we have received input and set our ordered_dict items we can loop through and print out the item and total price 
for key, value in ordered_dictionary.items():
    print(f'{key} {value}')



#### **SwapCase - Challenge** ####
# You are given a string and your task is to swap cases. In other words, convert all 
# lowercase letters to uppercase letters and vice versa.
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string s.
def swap_case(s):
    swap_values = []
    for char in s:
        if char.isalpha():
            if char.islower():
                swap_values.append(char.upper())
            else:
                swap_values.append(char.lower())
        else:
            swap_values.append(char)
    return (s, swap_values, ''.join(swap_values))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

## Output for above - Simple need to return the join statement for the test cases to pass
# ('HackerRank.com presents "Pythonist 2".', 
# ['h', 'A', 'C', 'K', 'E', 'R', 'r', 'A', 'N', 'K', '.', 'C', 'O', 'M', ' ', 'P', 'R', 'E', 'S', 'E', 'N', 'T', 'S', ' ', '"', 'p', 'Y', 'T', 'H', 'O', 'N', 'I', 'S', 'T', ' ', '2', '"', '.'], 
# 'hACKERrANK.COM PRESENTS "pYTHONIST 2".')


#### **String Split and Join - Challenge** ####
# In Python, a string can be split on a delimiter.

# Example:

# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 
def split_and_join(line):
    # write your code here (join method can use a separator to join the different indexes in the list item passed to it)
    # default to split on the white
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#### **What's Your Name - Challenge** ####
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Function Description

# Complete the print_full_name function in the editor below.

# print_full_name has the following parameters:

# string first: the first name
# string last: the last name
# Prints

# string: 'Hello firstname lastname! You just delved into python
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# Return statement by itself didn't work
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')
    return f'Hello {first} {last}! You just delved into python.'

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



#### **Strings - Mutations** ####
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.
# Example

# >>> string = "abracadabra"
# You can access an index by:

# >>> print string[5]
# a
# What if you would like to assign a value?

# >>> string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment


## Approaches
# Example

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
# Another approach is to slice the string and join it back.
# Example

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

## Task ##
# Read a given string, change the character at a given index and then print the modified string.
# Function Description

# Complete the mutate_string function in the editor below.

# mutate_string has the following parameters:

# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



#### **Find a String** ####
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring 
# occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2
def count_substring(string, sub_string):
    # So we need to loop through the string but at each index 
    # then loop through the length of the sub_string as recurring characters are allowed to generate the pattern
    # so we would only want to loop through the base_str for as long as a sub_str value could be
    # ABCDCDC - 7, CDC - 3 = So we only want to loop up to 3 characters from the end of the original string
    total_str_len = len(string)
    sub_str_len = len(sub_string)
    # range leaves us one short so samp_str[:4] wouldn't get the second c (:upuntilvalue)
    # This is all done so we don't get an index out of range error
    sub_str_count = 0
    for char_idx in range((total_str_len - sub_str_len) + 1):
        if string[char_idx:(char_idx+sub_str_len)] == sub_string:
            sub_str_count += 1
    return sub_str_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
