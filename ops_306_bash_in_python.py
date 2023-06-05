#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 06
# Author:                       David Prutch
# Date of latest revision:      06/06/2023
# Purpose:                      Execute Linux terminal commands from a Python script

# Import Libraries
# Import the OS to utilize Bash commands
import os
# Import the subprocess module
import subprocess

# Declaration of variables
# Creates variables which are set to output of respective bash command. 
# os-system command invokes the OS to run the command.
# Gets user name
user = os.system("whoami")
user1 = subprocess.run("whoami", capture_output=True)
# Gets IP address data
ip = os.system("ip a")
ip1 = subprocess.run(["ip", "a"], capture_output=True)
# Gets system information
short_info = os.system("sudo lshw -short")
short_info1 = subprocess.run(["sudo", "lshw", "-short"], capture_output=True)
# Declaration of functions


# Main
# Print each variable to the terminal usint print() function
print (user)
print (ip)
print (short_info)
print (user1)
print (ip1)
print (short_info1)
# End