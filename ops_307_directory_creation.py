#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 06
# Author:                       David Prutch
# Date of latest revision:      06/07/2023
# Purpose:                      Execute Linux terminal commands from a Python script

# Import libraries

import os

# Declaration of variables

inp = input("Please enter a directory path: ")

# Declaration of functions
def copy_dir(x): 
    for (root, dirs, files) in os.walk(x):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)



# Main
copy_dir(inp)

# End