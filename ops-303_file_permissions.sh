#!/bin/bash

# Script Name:                  Ops 301d8 Challenge 03
# Author:                       David Prutch
# Date of latest revision:      06/01/2023
# Purpose:                      Script allow user to select a directory and change the file permissions of all the files contained within.

# Declaration of variables
permissions=("File Permissions", "0:No Permissions", "1:Execute Only", "2:Write Only", "3:Write and Execute", "4:Read Only", "5:Read and Execute", "6:Read and Write", "7:Read, Write and Execute")

# Main
# Prompt user to provide directory absolute path to be used for file permission changes and read the answer storing it as the variable path.
echo "Please enter the absolute file path to the directory you would like to change the permissions for"
read path
# Display all file permissions.
for perm in "${permissions[@]}";
do
    echo $perm
done
# Prompt the user to input the permission values for each level of user as a 3 digit number, each between 0 and 7 read answer and store it as the variable ans. 
echo "from the listed permission options, enter 3 digits to update file permissions for Owner Group and Public , examples 755 or 312"
read ans
# Change permissions in the selected directory using chmod command.
chmod -R $ans $path
# Inform the user the permissions have been changed.
echo "Permissions have been changed"


# End