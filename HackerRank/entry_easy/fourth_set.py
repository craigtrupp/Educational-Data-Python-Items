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
from itertools import product
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
from itertools import product
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
