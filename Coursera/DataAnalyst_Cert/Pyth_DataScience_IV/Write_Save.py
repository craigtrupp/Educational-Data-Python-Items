#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:20:54 2022

@author: craigrupp
"""

# =============================================================================
# # Writing & Saving Files 
# =============================================================================


# We can open a file object using the method <code>write()</code> to save the text file to a list. 
# To write to a file, the mode argument must be set to **w**. Let’s write a file **Example2.txt** with the line: **“This is line A”**
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    
# Read File In to make sure it worked
with open(exmp2, 'r') as readfile:
    print(readfile.read())
    
# Write lines to file, Overwrite Existing File 
# Good practice to append the new line character at the end of your write statement
with open(exmp2, 'w') as writefile:
    writefile.write("This is line Y\n")
    writefile.write("This is line Z\n")
    
# Check multi-line doc
with open(exmp2, "r") as multilinefile:
    for line in multilinefile:
        print(line)
        

# List to write into .txt file
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
        
# We write a list to a .txt file as follows:
with open(exmp2, "w") as listwritefile:
    for line in Lines:
        print(f"Line to write to file : {line}")
        listwritefile.write(line)

# Verify List wiriting worked (should shee lines in list in read file)
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
# However, note that setting the mode to **w** overwrites all the existing data in the file.
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    

# =============================================================================
# Appending Files

# We can write to files without losing any of the existing data as follows by setting the mode argument to append: **a**.  
# See examples below
# =============================================================================
with open('Example2.txt', 'a') as appendfile:
    appendfile.write("First appended line\n")
    appendfile.write("Second appended line\n")
    appendfile.write("Last appended line\n")
    
# Valiedate appended file
with open('Example2.txt', 'r') as appendfilecheck:
    print(appendfilecheck.read())
    
    
# =============================================================================
# Additional Modes 
# It's fairly ineffecient to open the file in **a** or **w** and then reopening it in **r** to read any lines. 
# Luckily we can access the file in the following modes:

# *   r+ : Reading and writing. Cannot truncate the file.
# *   w+ : Writing and reading. Truncates the file.
# *   a+ : Appending and Reading. Creates a new file, if none exists.
#     
# =============================================================================

# Append onto existing file and read
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
    
# Note :  There were no errors but read() also did not output anything. This is because of our location in the file.
# =============================================================================
# Most of the file methods we've looked at work in a certain location in the file. 
# .write()  writes at a certain location in the file. 
# .read() reads at a certain location in the file and so on. 
# You can think of this as moving your pointer around in the notepad to make changes at specific location.
# =============================================================================
    

# =============================================================================
# Opening the file in w is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows. Whereas opening the file in a is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text.
# It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -
# 
# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
#     
# =============================================================================
    
# Revisit a+
with open('Example2.txt', 'a+') as testwritefile:
    # Where is cursor
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    # Move cursor (now data visible)
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    # See where curosr ends after being read after having the offset (seek) byte position changed
    print("Location after read: {}".format(testwritefile.tell()))
    

# Closing note on method [r,w,a]+
# =============================================================================
# Finally, a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however, opening a file in w+ overwrites it and deletes all pre-existing data.
# To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
# In the following code block, Run the code as it is first and then run it with the .truncate().
# =============================================================================
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    print('See existing txt file details')
    print(data)
    print('Set Curosr to Beginning')
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    
    
# =============================================================================
# # Copy A File
# =============================================================================
# Let's copy the file Example2.txt to the file Example3.txt:
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
                
# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
    
    


# =============================================================================
# # Exercise
# 
# Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.
# =============================================================================
#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


# Function Challenge
  
'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem, "r+") as readwritefile:
        #TODO: Open the exMem file in a+ mode
        with open(exMem, "a+") as appendfile:
        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Set cursor and bring lines into list, remove header
            readwritefile.seek(0)
            current_members = readwritefile.readlines()
            header = current_members[0]
            # Slice list to removed header at first position
            current_members = current_members[1:]
        #TODO: iterate through the members and create a new list of the innactive members (list comprehension with single condition)
            non_active = [innactive for innactive in current_members if ('no' in innactive)]
        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem
            readwritefile.seek(0)
            readwritefile.write(header)
            for member in current_members:
                if member not in non_active:
                    readwritefile.write(member)
                else:
                    appendfile.write(member)
            readwritefile.truncate()
    


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
    
    


                
    
    
    
    
    
    
    
    