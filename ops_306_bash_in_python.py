#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 06
# Author:                       David Prutch
# Date of latest revision:      06/06/2023
# Purpose:                      Execute Linux terminal commands from a Python script

# Import Libraries
# Import the subprocess module
import subprocess

# Declaration of variables
# Creates variables which are set to output of respective bash command. 
# os-system command invokes the OS to run the command.
# Gets user name
user = subprocess.run("whoami", capture_output=True)
# Gets IP address data
ip = subprocess.run(["ip", "a"], capture_output=True)
# Gets system information
short_info = subprocess.run(["sudo", "lshw", "-short"], capture_output=True)
# Declaration of functions


# Main
# Print each variable to the terminal usint print() function
# translate stdout to string

print (user.stdout.decode('utf=8'))
print (ip.stdout.decode('utf=8'))
print (short_info.stdout.decode('utf=8'))
# End