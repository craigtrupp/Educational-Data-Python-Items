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