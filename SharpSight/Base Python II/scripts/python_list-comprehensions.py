#################################################
# LIST COMPREHENSIONS
#
# How to ...
#   - create list comprehensions
#   - use list comprehensions, compared to loops
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
#################################################



#-----------------------
# ALTERNATIVE 'FOR LOOP'
#-----------------------
new_list = []

for x in range(6):
    y = x * 2
    new_list.append(y)


#-------------------
# LIST COMPREHENSION
#-------------------
even_list = [x*2 for x in range(6)]

print(even_list)
type(even_list)


# =============================================================================
# Further Examples Playing Around With
# =============================================================================

hobbit = {'protagonist': 'Bilbo', 'age':44, True:'afraid', 101: ['Smeagle', 'Sauron']}
hobbit.keys()
hobbit[101]
[type(x) for x in hobbit.keys()]
hobbit.values()
[x for x in hobbit.values()]
[x for x in hobbit.keys()]
# type of nested coprehension in which a list return item can be iterated to find all the values in a hobbits keys (essentially raw hobbit.values())
[hobbit[i] for i in (x for x in hobbit.keys())]
[type(x) for x in hobbit.values()]
hobbit.values()



# END