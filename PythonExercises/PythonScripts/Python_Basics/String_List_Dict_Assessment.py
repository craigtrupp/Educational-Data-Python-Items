# 1. Return the first character of any string entered
def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

## Readout
# H
# P
# K

# 2. Return count of letters in a string
# count only alphabetic characters
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for char in string: 
        # Complete the if-statement using a string method. 
        if char.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

## readouts
# 17
# 16
# 21

# 3. Returned sorted distances (longest first)
def sort_distance(distances):
    return sorted(distances, reverse=True)


print(sort_distance([2,4,0,15,8,9])) # [15, 9, 8, 4, 2, 0]


# 4. Even Numbers
def even_numbers(first, last):
  return [x for x in range(first, last) if x % 2 == 0]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

## Readouts
# [4, 6, 8, 10, 12]
# [0, 2, 4, 6, 8]
# [2, 4, 6]


# 5. String formatting
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animal in animal_dict.keys():
        # Use a string method to format the required string.
        result += '\n{}'.format(animal) 
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

## Printou
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger


# 6. Accept Two Dictionaries, Combine into one (each key listed once), "values" for first dict take precedence (if key in both dictionaries)
def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


## Print out
{'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


# 7. 
def setup_gradebook(old_gradebook):
    new_gradebook = old_gradebook.copy()
    for student in new_gradebook.keys():
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
#  output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

