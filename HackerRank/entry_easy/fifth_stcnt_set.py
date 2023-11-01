#### ** Sets Mutations ** #### 
# We can use the following operations to create mutations to a set:

# .update() or |=
# Update the set by adding elements from an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.update(R)
# >>> print H
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.intersection_update(R)
# >>> print H
# set(['a', 'k'])
# .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'r'])
# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.symmetric_difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'n', 'r', 'R'])

# TASK
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A.
# Should be similar to fifth_set with **getattr(set, operation)** then invoke a variable with the unique function for the set 


## Input
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

## Output - Just after Intersection Update (Code First)
# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A_len, set_A = int(input()), set(map(int, input().split()))
# now loop through the amount of method calls to make
for _ in range(int(input())):
    set_operation_n_len = input().split()
    set_op, set_len = getattr(set_A, set_operation_n_len[0]), set_operation_n_len[-1]
    n_set = set(map(int, input().split()))
    print(set_A, n_set, set_op, sep='\n')
    set_op(n_set)
    print(set_A)
    break

## Ouptut - We can see how the code can then move through the rest of the input
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 52, 24}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
# <built-in method intersection_update of set object at 0x7f8a3a7f0c80>
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}

### Solution for Set Mutations - key in assigning a string method to it's module (in this case a set)
# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A_len, set_A = int(input()), set(map(int, input().split()))
# now loop through the amount of method calls to make
for _ in range(int(input())):
    set_operation_n_len = input().split()
    set_op, set_len = getattr(set_A, set_operation_n_len[0]), set_operation_n_len[-1]
    n_set = set(map(int, input().split()))
    # Have our unique set operation assigned to set_op variable and new set from subsequent input value
    # Invoke to mutate the parent set (set_A) in place and following iterations, sum the values in the parent set
    set_op(n_set)
print(sum(set_A))


#### **Captain's room** #### 
# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. 
# The list consists of the room numbers for all of the tourists. 
# The room numbers will appear K times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

## Starter Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k_size_group = int(input())
room_number_list = input().split()
counter_items = Counter(room_number_list).items()
print(k_size_group, room_number_list, Counter(room_number_list), counter_items, sep='\n')
# 5
# ['1', '2', '3', '6', '5', '4', '4', '2', '5', '3', '6', '1', '6', '5', '3', '2', '4', '1', '2', '5', '1', '4', '3', '6', '8', '4', '3', '1', '5', '6', '2']
# Counter({'1': 5, '2': 5, '3': 5, '6': 5, '5': 5, '4': 5, '8': 1})
# dict_items([('1', 5), ('2', 5), ('3', 5), ('6', 5), ('5', 5), ('4', 5), ('8', 1)])

# Enter your code here. Read input from STDIN. Print output to STDOUT - Solution Code
from collections import Counter
k_size_group = int(input())
room_number_list = input().split()
counter_items = Counter(room_number_list).items()
captains_room = [x[0] for x in counter_items if x[1] != k_size_group]
print(''.join(captains_room))
## Printed 8 (without the join it was value in a list so .. yeah)


#### **Sets : Check Subset** ###
# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format

# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

# Enter your code here. Read input from STDIN. Print output to STDOUT - Solution Code
test_cases = int(input())
for _ in range(test_cases):
    A_element_count = int(input())
    A_set = set(map(int, input().split()))
    B_element_count = int(input())
    B_set = set(map(int, input().split()))
    A_interesect_B = A_set.intersection(B_set)
    print([True if len(A_interesect_B) == A_element_count else False][0])

## Test Input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

## Test Output - Need to index so as to not print the list value but rather the declaration of True/False
# True
# False
# False