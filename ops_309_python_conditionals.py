#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 09
# Author:                       David Prutch
# Date of latest revision:      06/09/2023
# Purpose:                      Working with Python Conditional Statements


# Import libraries

# Declaration of variables
num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
# Declaration of functions
def number_comparison(a, b):
    if a == b:
        print(a, "is equal to", b)
    elif a != b:
        print(a, "is not equal to", b)
        if a < b:
            print(a, "is less than", b)
        elif a > b:
            print(a, "is greater than", b)
    else:
        print("I am not sure")

def less_greater_equal(a, b):
    if a <= b and a < b:
        print(a, "is less than or equal to", b)
    elif a >= b and a > b:
        print(a, "is greater than or equal to", b)
    else:
        print("I am not sure")
# Main
less_greater_equal(num1, num2)
print("lets take a closer look at", num1, "and", num2)
number_comparison(num1, num2)
# End