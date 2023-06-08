#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 08
# Author:                       David Prutch
# Date of latest revision:      06/08/2023
# Purpose:                      This script creates and manipulates Lists in Python


# Import libraries

# Declaration of variables
# Assign to a variable a list of ten string elements.
list_items = ["candy", "fruit", "veggies", "beef", "chicken", "eggs", "bread", "milk", "pasta", "ice cream"]
# Declaration of functions

# Main
# Print the fourth element of the list.
# Using the index
print("Here is the fourth item in the list:")
print(list_items[3])
# Print the sixth through tenth element of the list.
# using the index range - leaving the end range blank will include the last element.
print("Thes are items 6 - 10 in the list:")
for items in list_items[5:]:
    print (items)
# Change the value of the seventh element to “onion”.
print("We are now changing list item seven from ", list_items[6], "to the following:")
list_items[6]="onion"
print(list_items[6])
print("Here is the updated list")
for items in list_items:
    print(items)
# End