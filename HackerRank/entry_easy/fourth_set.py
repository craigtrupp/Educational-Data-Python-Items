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


### Ok ... now the key for which we sorting for didn't take all the test cases ... because drr
## you need to dynamically acount for K which can be X characters that we want to make a permutation of 
# So we need to figure out how long the tuple we pased to the key parameter is based on K (2, 3, etc)

## So we need to kinda have a way to interpret a value to a tuple so we can then transform (not as straight forward as it would appear)
from ast import literal_eval as make_tupe
print(make_tupe("('x', 0)")) # ('x', 0)
print(make_tupe('(x[0])')) # ValueError: malformed node or string on line 1: <ast.Subscript object at 0x7f9969f98f10>

## ... ah man ... just looks liek the normal sort call on our list of tuples will work regardles of K 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
from ast import literal_eval as make_tupe
input_val = input().split()
S, k = input_val[0], int(input_val[1])
k_permutations = list(permutations(S, k))
k_permutations.sort() # super awesome sort method can dynamically sort in order of the permutation letter by tuple position so we don't need to use sorted with a key (which is ... I don't know how to create a tupe of indexes that was K length)
str_joined_tuples= [''.join(map(str, x)) for x in k_permutations] # make each tuple a str and join the values in a tuple
print('''{}'''.format('\n'.join(str_joined_tuples)))




#### **collections.Counter** ####
# Task

# Raghu is a shoe shop owner. His shop has N number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

