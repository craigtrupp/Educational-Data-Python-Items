#### **Cartesian Product** 
# itertools.product()

# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# >>> from itertools import product
# >>>
# >>> print list(product([1,2,3],repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# >>>
# >>> print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
# >>>
# >>> A = [[1,2,3],[3,4,5]]
# >>> print list(product(*A))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

#### Task
## You are given a two lists A and B. Your task is to compute their cartesian product X.

## Input Format
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.

# Both lists have no duplicate integer elements.

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
together = [x for x in [a, b]]
print(a,b,together)

## Input
# 1 2
# 3 4
## Output
# [1, 2] [3, 4] [[1, 2], [3, 4]] : a, b, then together for aboves


### Now the whole manual
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
together = [x for x in [a, b]]

## First way without the library (nested list comprehension)
cart_product_manual = [(x, y) for x in together[0] for y in together[1]]
#print(cart_product_manual) # [(1, 3), (1, 4), (2, 3), (2, 4)]
# Sample Output should be :  (1, 3) (1, 4) (2, 3) (2, 4)
cart_string = ''
for x in cart_product_manual:
    cart_string += f'{str(x)} '
print(cart_string.strip()) # make sure to trim trailing/leading space from str concatenation

# Output
(1, 3) (1, 4) (2, 3) (2, 4)

## With the itertools
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
together = [x for x in [a, b]] # [[1, 2], [3, 4]]
cartesian_product = list(product(*together))
#print(cartesian_product) # [(1, 3), (1, 4), (2, 3), (2, 4)]
str_ret = ''
for tup in cartesian_product:
    str_ret += f'{str(tup)} '
print(str_ret.strip())



#### **Itertools Permutations** #### 
# itertools.permutations(iterable[, r])

# This tool returns successive r length permutations of elements in an iterable.

# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>> 
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>> 
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# Task

# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Input Format

# A single line containing the space separated string S and the integer value k.



# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
input_val = input().split()
S, k = input_val[0], int(input_val[1])
print(S, k) # HACK 2
k_permutations = list(permutations(S, k))
print(k_permutations) # [('H', 'A'), ('H', 'C'), ('H', 'K'), ('A', 'H'), ('A', 'C'), ('A', 'K'), ('C', 'H'), ('C', 'A'), ('C', 'K'), ('K', 'H'), ('K', 'A'), ('K', 'C')]
# now we need to sort our permutation tuples 
# Sort list of tuples for lexicgoraphic sorted order
lex_order = sorted(k_permutations, key=lambda x: (x[0], x[1]))
print(lex_order) # [('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
print([f'{x[0]}{x[1]}' for x in lex_order]) # ['AC', 'AH', 'AK', 'CA', 'CH', 'CK', 'HA', 'HC', 'HK', 'KA', 'KC', 'KH']
print('''{}'''.format('\n'.join([f'{x[0]}{x[1]}' for x in lex_order])))
