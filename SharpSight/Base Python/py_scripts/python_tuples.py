##############################################################
# PYTHON TUPLES
#
# How to ...
#   - create tuples
#   - retrieve tuple items
#   - retrieve slices of tuples
#   - loop through a tuple
#   - perform tuple assignment
#   - delete a tuple
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
##############################################################



#~~~~~~~~~~~~~
# CREATE TUPLE
#~~~~~~~~~~~~~
coord_tuple = ('x', 'y', 'z')
type(coord_tuple)


#~~~~~~~~~~~~~~
# CREATE TUPLE
#~~~~~~~~~~~~~~
days = ('Mon','Tues','Wed','Thurs','Fri','Sat','Sun')
type(days)



#~~~~~~~~~~~~~~~~~~~~~~~~~~
# RETRIEVE ITEM FROM TUPLE
#~~~~~~~~~~~~~~~~~~~~~~~~~~
days = ('Mon','Tues','Wed','Thurs','Fri','Sat','Sun')


# Retrieve first item
days[0]


# Retrieve second item
days[1]


# Retrieve last item
days[-1]


#~~~~~~~~~~~~~~~~~~~~~~~~~~
# TAKE A SLICE OF A TUPLE
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# Get weekdays
days[0:5]



#~~~~~~~~~~~~~~~~~~~~~~
# LOOP THROUGH A TUPLE
#~~~~~~~~~~~~~~~~~~~~~~

for day in days:
    print(day)


#~~~~~~~~~~~~~~~~~~~~~~~
# CONVERT LIST TO TUPLE
#~~~~~~~~~~~~~~~~~~~~~~~

day_list = list(days)
type(day_list)

tuple(day_list)


#~~~~~~~~~~~~~~~~~~
# TUPLE ASSIGNMENT
#~~~~~~~~~~~~~~~~~~

# Create tuple
days = ('Mon','Tues','Wed','Thurs','Fri','Sat','Sun')


day_1 = days[0]
day_1
type(day_1)
# Assign tuple elements to new variable names
# – mon, tues, wed ... these are all new variable names 
(day_1, day_2, day_3, day_4, day_5, day_6, day_7) = days
day_8 = days[:1]
day_8
type(day_8)

print(day_1)
print(day_2)
print(day_3)
[print(type(day)) for day in [day_1, day_2, day_3]]
# tuple assignment to str if put in tuple () otherwise it's a tuple (see day_8)
#~~~~~~~~~~~~~~~~
# DELETE A TUPLE
#~~~~~~~~~~~~~~~~

del days[:1]
days


#END
