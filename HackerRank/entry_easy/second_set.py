## Tuples - Challenge
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


## Collections - OrderedDict Challenge
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
