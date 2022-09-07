#################################################
# LOOPS
#
# How to ...
#   - use for loops
#   - use while loops
#   – use the range() function
#   - use the break statement
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
#################################################



#==========
# FOR LOOPS
#==========

#--------------
# A SIMPLE LOOP
#--------------
mylist = [1,2,3]

for item in mylist:
    print(item)


#-----------------
# LOOP OVER A LIST
#-----------------
car_list = ['ferrari','porsche','bugatti']

for car in car_list:
    print(car)


#-------------------
# LOOP OVER A STRING
#-------------------
my_string = "Data"

for letter in my_string:
    print(letter)


#-------------------
# LOOP OVER A TUPLE
#-------------------
num_tup = (1,2,3,4)

for number in num_tup:
    print(number)

    
#========
# RANGES
#========

#-------------------------
# LOOP OVER A SIMPLE RANGE
#-------------------------
for number in range(4):
    print(number)

#-------------------------------    
# LOOP OVER A MORE COMPLEX RANGE
#-------------------------------
for number in range(2,11,2):
    print(number)



#============
# WHILE LOOPS
#============
counter = 0

while counter < 4:
    print(counter)
    counter += 1


#-----------------
# BREAK STATEMENTS
#-----------------
num_list = [1,2,3,42,5]

for number in num_list:
    print(number)
    if number == 42:
        print('we found it!')
        break


# END