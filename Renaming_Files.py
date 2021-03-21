### This function changes the names of files in a folder

## Importations
import os

## Path of the folder
path = "C:/Users/Owner/Desktop/Test_Folder/"

## Forloop to change names of files in the choosen folder
for filename in os.listdir(path):
    # Original path of the files
    original_filename = path + filename
    # Renaming convention
    new_filename = path + 'Old_' + filename
    # Renaming code to change the name itself
    os.rename(original_filename, new_filename)
    
## Notes - 
#   The new naming convention in this case is adding Old_ to the beginning
# of the previous file name.  Though this is not necessary.  You do not need
# to have the old filename if that is not desired.  An example of what I've
# seen is by adding a variable equal to one before the forloop, then include
# it into your renaming convention.  Afterwards putting a variable +=1 at
# the end fo the forloop to keep increasing the number.  Thus it will be
# name and a series of increasing numbers.

## example -
# count = 1
# new_filename = path + 'Sales_Report' + count
# count += 1
