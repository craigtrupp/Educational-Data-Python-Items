#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:49:04 2022

@author: craigrupp
"""

## Uncomment these if working locally, else let the following code cell run.

import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

## Download Example file
# !wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

# Open file in read mode
file1 = open(filename, 'r')
type(file1)
# Name of File
print(file1.name)
# Mode of file
print(file1.mode) #r (read)

# Read the files contents
FileContent = file1.read()
type(FileContent)
len(FileContent)
FileContent
filelist = FileContent.split("\n")
print(filelist)
# Turn list back to multi-line string 
multi_str = '\n'.join(filelist)
print(multi_str)
print([type(filelist), type(multi_str)])
# Close File
file1.close()


# With
# =============================================================================
# # Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. 
# # The code will run everything in the indent block then close the file object.
# =============================================================================
with open(filename, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    

# Verify above file (line #20 is closed)
file1.closed


print(FileContent)

# We don’t have to read the entire file, for example, we can read the first 4 characters by entering three as a parameter to the method **.read()**:
with open(filename, "r") as file1:
    print(file1.read(4))
    

# Once the method .read(4) is called the first 4 characters are called. If we call the method again, the next 4 characters are called. 
# The output for the following cell will demonstrate the process for different inputs to the method read():
# Read certain amount of characters

with open(filename, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    

# Read certain amount of characters
with open(filename, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
    
# .readline() File object method
# We can also read one line of the file at a time using the method <code>readline()</code>:

with open(filename, "r") as file1:
    print(f"First Line : {file1.readline()}")
    

# Single line restriction with .readline()
# We can also pass an argument to <code> readline() </code> to specify the number of charecters we want to read. 
# However, unlike <code> read()</code>, <code> readline()</code> can only read one line at most.
with open(filename, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate Through the Lines
with open(filename,"r") as file1:
        i = 0;
        print(type(file1))
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# We can use the method readlines() to save the text file to a list:
with open(filename, "r") as file1:
    FileasList = file1.readlines()

[print(x) for x in FileasList]
print(FileasList[0], len(FileasList))











    


