#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:45:52 2022

@author: craigrupp
"""

# Create a class Circle
import matplotlib.pyplot as plt
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

    
blu_3 = Circle() #Use default arguments
blu_3.radius
blu_3.drawCircle()
# Methods of Object
dir(blu_3)

orange_8 = Circle(8, 'Orange')
orange_8.drawCircle()


class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
        
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
SkinnyBlueRectangle.drawRectangle()


FatYellowRectangle = Rectangle(20, 5, 'yellow')
FatYellowRectangle.drawRectangle()


# Challenge
# =============================================================================
# Constructor (__init__) - This method should take the argument text, make it lower case, and remove all punctuation. Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called fmtText.
# freqAll - This method should create and return dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the fmtText attribute.
# freqOf - This method should take a word as an argument and return the number of occurrences of that word in fmtText.
# =============================================================================

class analysedText(object):   
    def __init__ (self, text):
        # TODO: Remove the punctuation from <text> and make it lower case.
        formattedText = text
        for character in ['.', '!', ',', '?']:
            formattedText = formattedText.replace(character, '')
        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = formattedText.lower() 
    
    def freqAll(self):    
        # TODO: Split the text into a list of words  
        words_list = self.fmtText.split(" ")
        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        freqDict = {}
        for word in words_list:
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
        
        return freqDict
        
    
    def freqOf(self, word):
        # TODO: return the number of occurrences of <word> in <fmtText>
        countDict = self.freqAll()
        if word in countDict:
            return countDict[word]
        else:
            return 0
        
    



text = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
formattedText = text
for character in ['.', '!', ',', '?']:
    formattedText = formattedText.replace(character, '')
formattedText = formattedText.lower()
formattedText.split(" ")
freqDict = {}

for word in formattedText.split(" "):
    if word in freqDict:
        freqDict[word] += 1
    else:
        freqDict[word] = 1

print(freqDict)




