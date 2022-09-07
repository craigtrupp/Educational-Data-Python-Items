##############################################################
# PYTHON LISTS
#
# How to ...
#   - create lists
#   - change tuples and sets into lists
#   - retrieve list items
#   - retrieve slices of lists
#   - modify lists
#   - delete items from lists
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
##############################################################



#------------
# CREATE LIST
#------------

# MANUALLY CREATE LIST
car_list = ['ferrari','porsche','bugatti']
type(car_list)
print(car_list)


# CREATE LIST FROM SET
japanese_car_set = {'honda', 'toyota'}
type(japanese_car_set)
print(japanese_car_set)
for i in japanese_car_set:
    print(i)
# Make sure to highlight the whole loop when looking to executed in kernel/console
japanese_car_list = list(japanese_car_set)
type(japanese_car_list)
print(japanese_car_list)


# CREATE LIST FROM TUPLE
german_car_tuple = ('audi', 'bmw')
german_car_list = list(german_car_tuple)



#----------------------
# REMOVE ITEM FROM LIST
#----------------------

car_list = ['ferrari','porsche','bugatti']
print(car_list)


car_list.remove('porsche')
print(car_list)



#-----------------
# ADD ITEM TO LIST
#-----------------

car_list = ['ferrari','porsche','bugatti']
print(car_list)


car_list.append('hennessey')
print(car_list)



#---------------------------
# EXTEND A LIST
# - i.e., add multiple items
#---------------------------

car_list = ['ferrari','porsche','bugatti']
print(car_list)


car_list.extend(['mclaren','aston martin'])
print(car_list)
car_list.extend('ford', 'honda')
#TypeError: list.extend() takes exactly one argument (2 given)

#----------------------------
# INSERT
# - insert new item into list
#----------------------------
car_list = ['ferrari','porsche','bugatti']


car_list.insert(2, 'bmw')
print(car_list)



#----------------------------------------
# COMBINE TWO LISTS ('CONCATENATE' LISTS)
#----------------------------------------
car_list = ['ferrari','porsche','bugatti']
extra_cars = ['mclaren','aston martin']


car_list_full = car_list + extra_cars
print(car_list_full)



#------------
# SORT A LIST
#------------

car_list_full = ['ferrari','porsche','bugatti','mclaren','aston martin']
print(car_list_full)


car_list_full.sort()
print(car_list_full)



#-------------------
# RETRIEVE LIST ITEM
#-------------------
car_list = ['ferrari','porsche','bugatti']


# Retrieve first list item
car_list[0]


# Retrieve second list item
car_list[1]


# Retrieve last list item
car_list[-1]



#---------------------------------
# RETRIEVE A 'SLICE' OF A LIST
#  - i.e., retrieve multiple items
#---------------------------------

car_list_full = ['ferrari','porsche','bugatti','mclaren','aston martin']

# Get first two items
car_list_full[0:2]


# Get all items from position 1 onward
car_list_full[1:]


# Get last two items
car_list_full[-2:]



#------------------------------
# REMOVE DUPLICATES FROM A LIST
# 1. Convert list to set
# 2. Convert set back to list
#------------------------------
car_list_withdupes = ['ferrari','porsche','mclaren','mclaren']
print(car_list_withdupes)


# DEDUPE: convert list to set
car_set_deduped = set(car_list_withdupes)
print(car_set_deduped)


# Convert set back to list
car_list_deduped = list(car_set_deduped)
print(car_list_deduped)



#-----------------------
# DELETE ITEMS FROM LIST
#-----------------------

# Delete by position
car_list = ['ferrari','porsche','bugatti']
del car_list[0]

print(car_list)


# Remove by item name
car_list = ['ferrari','porsche','bugatti']
car_list.remove('porsche')

print(car_list)



#---------------------------------------
# LOOP EXAMPLE
# - iterate through the items of a list
#   and use them in a print statement
#---------------------------------------

car_list = ['ferrari','porsche','bugatti']

for car in car_list:
    print('%s is a type of car' % car)


# END