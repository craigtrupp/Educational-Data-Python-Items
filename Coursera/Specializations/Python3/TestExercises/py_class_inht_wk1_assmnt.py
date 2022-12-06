## Queston 1
# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. 
# The constructor should initialize two instance variables: apple_color and apple_quantity. 
# Write a class method called increase that increases the quantity by 1 each time it is invoked. 
# You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." 
# (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)


class AppleBasket:
    def __init__(self, color, quantity):
        self.apple_color = str(color)
        self.apple_quantity = int(quantity)
        
    def increase(self):
        self.apple_quantity += 1
        
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
    
blue_5 = AppleBasket('blue', 50)
print(blue_5)
# A basket of 50 blue apples.


## Question 2 
# Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. 
# The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, 
# you see "Your account, [name goes here], has [start_amt goes here] dollars." 
# Create an instance of this class with "Bob" as the name and 100 as the amount. 
# Save this to the variable t1.

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amt = amount

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)

t1 = BankAccount("Bob", 100)
print(t1)
# Your account, Bob, has 100 dollars.
