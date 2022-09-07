#################################################
# IF/ELSE STATEMENTS
#
# How to ...
#   - use the 'if' keyword
#   - use if/else statements
#   - use if/elif/else statements
#   - use code blocks
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
#################################################



#-----------------
# THE 'IF' KEYWORD
#-----------------
volume = 11

if volume == 11:
    print('This one goes to eleven.')



#-------------------
# IF/ELSE STATEMENTS
#-------------------

x = 42

if x > 0:
    print('greater than 0')
else:
    print('less than or equal to 0')



#--------------------
# IF/ELIF STATEMENTS
#--------------------

city = 'Chicago'

if city == 'Cleveland':
    print('Hello Cleveland!')
elif city == 'New York':
    print('Hello New York!')
elif city == 'Chicago':
    print('Hello Chicago!')



#-------------------------
# IF/ELIF/ELSE STATEMENTS
#-------------------------

city = 'Austin'

if city == 'Cleveland':
    print('Hello Cleveland!')
elif city == 'New York':
    print('Hello New York!')
elif city == 'Chicago':
    print('Hello Chicago!')
else:
    print('Where are we?')

city = 'Abq'

if city == 'Abq':
    print('Hello Cleveland!')
elif city == 'Abq':
    print('Hello New York!')
elif city == 'Chicago':
    print('Hello Chicago!')
else:
    print('Where are we?')

# Should you want multiple conidtions caught, multiple if statements needed    
city = 'SantaFe'

if city == 'SantaFe':
    print('Hello Cleveland!')
if city == 'SantaFe':
    print('Hello New York!')
elif city == 'Chicago':
    print('Hello Chicago!')
else:
    print('Where are we?')




# END