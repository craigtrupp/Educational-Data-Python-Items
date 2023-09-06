# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day. 


import email


def sum_server_use_time(Server):

    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items 
    # using a for loop. Tuple return and then just accessing dictionary argument with each key for the value
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]
        
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # print 20.1



# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.  
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    # key, value to unpack the tuple values from the return of .items()
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        # recall the tuple value in the unpacked argument is a list allowing to iterate over the key's list value
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name". 
            full_names.append(first_name+" "+last_name)
            
    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations. 
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']



# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 


def invert_resource_dict(resource_dictionary):
  # Initialize a "new_dictionary" variable as a dict data type using
  # empty {} curly brackets. 
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the 
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


##### Dictionary comprehension Examples 
words = ['data', 'science', 'machine', 'learning']
#list comprehension
[len(i) for i in words]
[4, 7, 7, 8]
#dictionary comprehension
print({i:len(i) for i in words})
## {'data': 4, 'science': 7, 'machine': 7, 'learning': 8}

# Conditional setting using the index of each word in the list as the key and it's length as the value
print({i:len(i) for i in words if len(i) > 5})
## {'science': 7, 'machine': 7, 'learning': 8}

## with an else
words_dict = {i:len(i) if len(i) > 5 else 'short' for i in words}
print(words_dict)
## {'data': 'short', 'science': 7, 'machine': 7, 'learning': 8}

## Iterate over two variables (use zip)
values = [5, 3, 1, 8]
dict_a = {i:j for i, j in zip(words, values)} # zip needs to sequences (items of the same length)
print(dict_a)
## {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}

## with a Condition (added to above reference)
dict_a = {i:j for i, j in zip(words, values) if j > 4}
print(dict_a)
## {'data': 5, 'learning': 8}


## Transformations on key-value pairs
dict_b = {i.upper():j**2 for i, j in zip(words, values)}
print(dict_b)
## {'DATA': 25, 'SCIENCE': 9, 'MACHINE': 1, 'LEARNING': 64}


### Index : Enumeration (The enumerate function of Python can be used to create an iterable of tuples based on a list. Each tuple contains the items in the list with incrementing integer values.)
names = ['John', 'Jane', 'Adam', 'Eva', 'Ashley']
print(list(enumerate(names)))
## [(0, 'John'), (1, 'Jane'), (2, 'Adam'), (3, 'Eva'), (4, 'Ashley')]

## Now to use enumerate in a dict_comprehension
print({idx:len(name) for idx, name in enumerate(names)})
## {0: 4, 1: 4, 2: 4, 3: 3, 4: 6}

## If you just want to create a dictionary based on a list of tuples without any modification on the values, you do not need to use a comprehension. The dict function will do the job.
print(dict(enumerate(names)))
## {0: 'John', 1: 'Jane', 2: 'Adam', 3: 'Eva', 4: 'Ashley'}

### Keys of Tuples (Nested Loops)
a = [1,2,3,4]
b = [5,6,7]
dct = {(i,j):i*j for i in a for j in b}
print(dct)

## {(1, 5): 5, (1, 6): 6, (1, 7): 7, (2, 5): 10, (2, 6): 12, (2, 7): 14, (3, 5): 15, (3, 6): 18, (3, 7): 21, (4, 5): 20, (4, 6): 24, (4, 7): 28}


## Quiz
# 1 : Generate list that contains complete email addresses
def email_list(domains):
    emails = []
    for email_signature, address_list in domains.items():
        email_sig_list = [x+'@'+email_signature for x in address_list]
        emails.extend(email_sig_list)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
## ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']
 

# 2: The groups_per_user function receives a dictionary, which contains group names with a list of users. Users can belong to multiple groups.
# Return a dictionary with **users as keys and a list of their groups as values**
def groups_per_user(group_dictionary):
	# Let's get the unique user types first values returns a list for each key's value which will need to flatten
    users = [user for sublist in list(group_dictionary.values()) for user in sublist] # returns : ['admin', 'userA', 'admin', 'userB', 'admin']
    # Use set/list to modify users for only unique
    users = list(set(users)) # returns : ['admin', 'userA', 'userB']
    # Add unique user keys to user_groups
    user_groups = {user:[] for user in users} # dictionary comprehension to give each unique user an empty list (will add different groups next)
    # Loop through users
    for user in users:
        # loop through each key
        for group in group_dictionary.keys():
            # see if user is in the dictionary key passed to arg
            if user in group_dictionary[group]:
                user_groups[user].append(group)
    return user_groups

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"]}))
# {'userB': ['public'], 'userA': ['local'], 'admin': ['local', 'public', 'administrator']}


## 3. Update return
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
## Essentially the new_times dictionary replace any key/value pairs for found similar keys (so jeans from wardrobe initially is changed to that key's new value in new_items)
## {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}


## 5. 
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))
# 28.44 
