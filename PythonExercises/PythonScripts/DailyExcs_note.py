""" Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. 
Then, find the key with the highest value in this dictionary and assign that key to max_value. """

product = "iphone and android phones"
lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d.setdefault(char, 1)
    else:
        lett_d[char] += 1

values_high_low = sorted(lett_d.values(), reverse=True)
max_value = max(lett_d, key=lambda x: lett_d[x]) # max key
print(max_value, max_value in lett_d)
print(values_high_low)
print(lett_d)

# n True
# [4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]
# {'i': 2, 'p': 2, 'h': 2, 'o': 3, 'n': 4, 'e': 2, ' ': 3, 'a': 2, 'd': 3, 'r': 1, 's': 1}


"""Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. 
mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then 
returns the result."""

def addit(nmb):
    return nmb + 5

def mult(nmb):
    return nmb * addit(nmb)

print(mult(5)) # 50