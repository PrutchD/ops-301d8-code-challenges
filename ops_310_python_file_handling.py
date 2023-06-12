#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 10
# Author:                       David Prutch
# Date of latest revision:      06/12/2023
# Purpose:                      Working with Python file handling


# Import libraries

# Declaration of variables
# Variable to hold new file name
file = "test_file.txt"

# Declaration of functions
# Create File Function 
def create_file(file_name):
    new_file = open(file_name, "w")
    new_file.close()

# Append File Function
# Asks user for input then appends new line to input
# Appends augmented input to file
# Repeats 3 times
def append_file(file_name1):
    counter = 0
    append = open (file_name1, "a")
    while counter < 3:
        inp = input("What would you like to add to the next available line of " + file_name1 + "?: ")
        inp = inp + " \n"
        append.write(inp)
        counter += 1
    append.close()

# Reading the file Function
# Reads the file, saves it in a list
# Prints selected line from the file using the list index
def read_file(file_name3):
    file_name3 = open("test_file.txt", "r")
    content = file_name3.readlines()
    print(content[0])
    file_name3.close()
# Main
create_file(file)
append_file(file)
read_file(file)
# End