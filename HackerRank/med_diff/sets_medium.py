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