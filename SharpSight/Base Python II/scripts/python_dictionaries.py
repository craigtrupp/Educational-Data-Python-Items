##############################################################
# PYTHON DICTIONARIES
#
# How to ...
#   - create dictionaries
#   - retrieve keys and values from a dictionary
#   - remove items
#   - add items
#   - use dictionaries to solve problems (example use cases)
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
##############################################################


#------------------
# CREATE DICTIONARY
#------------------
parking_spots = { 101:'Ferrari'
                 ,102:'Bugatti'
                 ,103:'Porsche'
                 ,104:'Mclaren'
                }

print(parking_spots)


#---------
# GET ITEM
#---------
parking_spots[103]


#------------
# REMOVE ITEM
#------------
del parking_spots[103]

print(parking_spots)


#-------------
# ADD NEW ITEM
#-------------
parking_spots[105] = 'Tesla'

print(parking_spots)


#===================
# DICTIONARY METHODS
#===================

# GET KEYS
parking_spots.keys()


# GET VALUES
parking_spots.values()


# GET ITEMS
parking_spots.items()
[x[0] for x in parking_spots.items()]
[[x[0], x[1], (x[0], x[1])] for x in parking_spots.items()]
# REMOVE ALL ITEMS
parking_spots.clear()

print(parking_spots)


#------------------------------------
# LOOP EXAMPLE
# - iterate through the items
#   and use them in a print statement
#------------------------------------

# CREATE
parking_spots = { 101:'Ferrari'
                 ,102:'Bugatti'
                 ,103:'Porsche'
                 ,104:'Mclaren'
                }

print(parking_spots)


# LOOP - key, value in dict.items()
for parking_spot, car in parking_spots.items():
    print('The %s is in parking spot %s' % (car, parking_spot))



#======================
# USE CASE: XREF TABLES
#======================

#------------------
# MILITARY ALPHABET
#------------------
military_alphabet = { 'a':'alfa'
                     ,'b':'bravo'
                     ,'c':'charlie'
                     ,'d':'delta'
                     ,'e':'echo'
                     ,'f':'foxtrot'
                     ,'g':'golf'
                     ,'h':'hotel'
                     ,'i':'india'
                     ,'j':'julia'
                     ,'k':'kilo'
                     ,'l':'lima'
                     ,'m':'mike'
                     ,'n':'november'
                     ,'o':'oscar'
                     ,'p':'papa'
                     ,'q':'quebec'
                     ,'r':'romeo'
                     ,'s':'siera'
                     ,'t':'tango'
                     ,'u':'uniform'
                     ,'v':'victor'
                     ,'w':'whiskey'
                     ,'x':'xray'
                     ,'y':'yankee'
                     ,'z':'zulu'
                }



# RETRIEVE CODE WORDS FOR LETTERS
military_alphabet['p']
military_alphabet['y']
military_alphabet['t']
military_alphabet['h']
military_alphabet['o']
military_alphabet['n']



# USE LOOP TO SPELL 'python' IN MILITARY CODE WORDS
for letter in 'python':
    print(military_alphabet[letter])



#------------
# STATE CODES
#------------

state_name_lookup = { 'AL':'Alabama'
                     ,'AK':'Alaska'
                     ,'AZ':'Arizona'
                     ,'AR':'Arkansas'
                     ,'CA':'California'
                     ,'CO':'Colorado'
                     ,'CT':'Connecticut'
                     ,'DE':'Delaware'
                     ,'FL':'Florida'
                     ,'GA':'Georgia'
                     ,'HI':'Hawaii'
                     ,'ID':'Idaho'
                     ,'IL':'Illinois'
                     ,'IN':'Indiana'
                     ,'IA':'Iowa'
                     ,'KS':'Kansas'
                     ,'KY':'Kentucky'
                     ,'LA':'Louisiana'
                     ,'ME':'Maine'
                     ,'MD':'Maryland'
                     ,'MA':'Massachusetts'
                     ,'MI':'Michigan'
                     ,'MN':'Minnesota'
                     ,'MS':'Mississippi'
                     ,'MO':'Missouri'
                     ,'MT':'Montana'
                     ,'NE':'Nebraska'
                     ,'NV':'Nevada'
                     ,'NH':'New Hampshire'
                     ,'NJ':'New Jersey'
                     ,'NM':'New Mexico'
                     ,'NY':'New York'
                     ,'NC':'North Carolina'
                     ,'ND':'North Dakota'
                     ,'OH':'Ohio'
                     ,'OK':'Oklahoma'
                     ,'OR':'Oregon'
                     ,'PA':'Pennsylvania'
                     ,'RI':'Rhode Island'
                     ,'SC':'South Carolina'
                     ,'SD':'South Dakota'
                     ,'TN':'Tennessee'
                     ,'TX':'Texas'
                     ,'UT':'Utah'
                     ,'VT':'Vermont'
                     ,'VA':'Virginia'
                     ,'WA':'Washington'
                     ,'WV':'West Virginia'
                     ,'WI':'Wisconsin'
                     ,'WY':'Wyoming'                     
                     }

print(state_name_lookup)


# LOOK UP STATE NAMES FROM ABBREVIATIONS
state_name_lookup['TX']
state_name_lookup['ME']



#END