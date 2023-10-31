#### **Sets : Intro to Sets** ####
# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 
# Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used: avg = sum_distinct_heights / total_distinct_heights

# >>> list(map(int, '1 3 5 9 11 35'.split()))
# [1, 3, 5, 9, 11, 35] - Quick reminder of some of the logc in the main function below

def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



#### ** Sets: Symmetric Difference ** ####
# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both. (anti-join)

# Input Format

# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
sym_diff = a.symmetric_difference(b) 
print(*sorted(list(sym_diff)), sep='\n')




#### ** Sets : No Idea - Happiness Index (This one was considered Medium Difficulty) ** ####
# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
# For each i integer in the array, if i intersects with set A, you add 1 to your happiness. 
# If i intersect with set B, you add -1 to your happiness. Otherwise, your happiness does not change. 
# Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. 
# However, the array might contain duplicate elements.

# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# Sample Input
# 3 2
# 1 5 3
# 3 1
# 5 7

# Sample Output
# 1

# Explanation

# You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. 
# The element 7 in set B does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is 2 - 1 = 1.

# Enter your code here. Read input from STDIN. Print output to STDOUT
array_integers, sets = list(map(int, input().split()))
print(array_integers, sets) # unpack first two arguments into array_integers and sets as ints
happiness = 0
array_vals = [int(x) for x in input().split()] 
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
print(array_vals, A, B, sep='\n')

## Output 
# 3 2
# [1, 5, 3]
# {1, 3}
# {5, 7}


## Now to Solve (Above just some fun)
# Enter your code here. Read input from STDIN. Print output to STDOUT
array_integers, sets = list(map(int, input().split()))
#print(array_integers, sets) # unpack first two arguments into array_integers and sets as ints
happiness = 0
array_vals = [int(x) for x in input().split()] 
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
for val in array_vals:
    if val in A:
        happiness += 1
    if val in B:
        happiness -= 1
print(happiness)



#### **Set.add()** 
# Task

# Apply your knowledge of the .add() operation to help your friend Rupal.
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
# She asked for your help. You pick the stamps one by one from a stack of N country stamps.

# Find the total number of distinct country stamps.
# Input Format

# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Probably a bit easier with a set comprehension but we'll do both
# Enter your code here. Read input from STDIN. Print output to STDOUT
country_lines = int(input())
print(country_lines)
country_set = {str(input()) for _ in range(country_lines)}
print(country_set, len(country_set))

## Set Comprehension output
# 7
# {'China', 'USA', 'New Zealand', 'France', 'UK'} 5

## Using .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
country_lines = int(input())
country_set = set()
for _ in range(country_lines):
    country_set.add(str(input()))
print(country_set, len(country_set))

# {'France', 'UK', 'USA', 'China', 'New Zealand'} 5


#### **Set functions - discard(), remove(), & pop()**

# .remove(x)
# This operation removes element x from the set.
# If element x does not exist, it raises a KeyError.
# The .remove(x) operation returns None.

# .discard(x)
# This operation also removes element x from the set.
# If element x does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.

# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.

# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Output Format

# Print the sum of the elements of set s on a single line.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

## See below for an initial unpacking of the type operation to perform on a set from the passed argument in an input
n = int(input())
s = set(map(int, input().split()))
print(n)
print(s)
for _ in range(int(input())):
    set_operations = input().split()
    # print(set_operations) # ['pop'], ['remove', '9'] (two sample input values)
    if len(set_operations) == 1:
        single_set_operation = getattr(set, set_operations[0])
        print(single_set_operation)
    break

## Output - See print statement and how a single operation for our object type can be retrieved w/getattr
# 9
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# <method 'pop' of 'set' objects>

### Output with custom read out for future reference
n = int(input())
s = set(map(int, input().split()))
print(n)
print(s)
for x in range(int(input())):
    set_operations = input().split()
    # print(set_operations) # ['pop'], ['remove', '9'] (two sample input values)
    if len(set_operations) == 1:
        # attaches the string module (set) function from the passed argument which we can try and call
        single_set_operation = getattr(s, set_operations[0])
        try:
            single_set_operation()
        except KeyError as e:
            print(f"{single_set_operation} unable to be performed due to a {e}")
            continue
    else:
        set_opp, value = getattr(s, set_operations[0]), int(set_operations[-1])
        try:
            set_opp(value)
        except KeyError:
            continue
    print(f'Value of set s : {s} after loop iteration : {x + 1} with set_operation {set_operations}')
print(s)

## Output - Here they just want the sum of the remaining integers so we would just print sum(set(s)) 
# 9
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Value of set s : {2, 3, 4, 5, 6, 7, 8, 9} after loop iteration : 1 with set_operation ['pop']
# Value of set s : {2, 3, 4, 5, 6, 7, 8} after loop iteration : 2 with set_operation ['remove', '9']
# Value of set s : {2, 3, 4, 5, 6, 7, 8} after loop iteration : 3 with set_operation ['discard', '9']
# Value of set s : {2, 3, 4, 5, 6, 7} after loop iteration : 4 with set_operation ['discard', '8']
# Value of set s : {2, 3, 4, 5, 6} after loop iteration : 5 with set_operation ['remove', '7']
# Value of set s : {3, 4, 5, 6} after loop iteration : 6 with set_operation ['pop']
# Value of set s : {3, 4, 5} after loop iteration : 7 with set_operation ['discard', '6']
# Value of set s : {3, 4} after loop iteration : 8 with set_operation ['remove', '5']
# Value of set s : {4} after loop iteration : 9 with set_operation ['pop']
# Value of set s : {4} after loop iteration : 10 with set_operation ['discard', '5']
# {4}
            
    

