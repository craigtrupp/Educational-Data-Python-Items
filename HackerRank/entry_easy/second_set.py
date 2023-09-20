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


