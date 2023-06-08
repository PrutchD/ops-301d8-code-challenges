#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 06
# Author:                       David Prutch
# Date of latest revision:      06/07/2023
# Purpose:                      Use os.walk() function to map out directories

# Import libraries

import os

# Declaration of variables

inp = input("Please enter a directory path: ")

# Declaration of functions
def copy_dir(x): 
    for (root, dirs, files) in os.walk(x):
        # Print root
        print(root)
        # Print directories
        print(dirs)
        # Print files
        print(files)



# Main
copy_dir(inp)

# End