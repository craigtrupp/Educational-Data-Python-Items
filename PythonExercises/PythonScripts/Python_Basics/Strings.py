def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":
            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string += letter
            reverse_string = new_string[::-1]

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code.
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True
		
    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

## Read Outs
# True
# False
# True



def convert_distance(miles):
    km = round(miles * 1.6, 2)
    result = "{} miles equals {} km".format(miles, km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

## Read Outs
# 12 miles equals 19.2 km
# 5.5 miles equals 8.8 km
# 11 miles equals 17.6 km


def nametag(first_name, last_name):
    return("{} {}.".format(first_name.title(), last_name.title()[0]))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


## Read Out
# Jane S.
# Francesco R.
# Jean-Luc G.



def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence
    # split on white space (get last word)
    sentence_last_word = sentence.split(' ')[-1]
    if old == sentence_last_word:
        new_sentence = sentence.split()[:-1] # get all words until last item
        new_sentence.append(new)
        return ' '.join(new_sentence)
    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


## Readouts
# It's raining cats and dogs
# She sells seashells by the seashore
# The weather is nice in May
# The weather is nice in April