#!/bin/bash

# Script Name:                  Ops 301d8 Challenge 02
# Author:                       David Prutch
# Date of latest revision:      06/02/2023
# Purpose:                      This script will allow a user to select different options from and menu which will be executed.
#                               This will be run in a loop so the user can run any of the options as many times as they want or they can exit.

# Declaration of variables
# Array to hold menu options
menu_items=("1: Print Hello World", "2: Ping my PC", "3: Display my IP information", "4: Exit")
# get the users ip address, not net tools needs to be installed use: sudo apt install net-tools.

# Declaration of functions

# Main
while true
do 
    # displays the menu to the user
    for menu in "${menu_items[@]}";
    do 
        echo $menu
    done
    # asks the user to pick a menu option and stores the input in selection variable. trying th read -p command for the first time.
    echo "Please make a selection from the menu " 
    read selection
    # if user selects 1 Hello World is printed in the terminal then the loop repeats.
    if [ $selection -eq 1 ] ; then
        echo "Hello World"
    # If user selects 2 a self ping is executed then the loop repeats.
    elif [ $selection -eq 2 ] ; then
        # Attribution https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x
        # -c limits number of attempts.
        ping -c5 $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')
    # If the user selects 3 their IP information is displayed then the loop repeaats.
    elif [ $selection -eq 3 ] ; then
        ifconfig
    # If the user selects 4 the loop is broken and the script ends.
    elif [ $selection -eq 4 ] ; then
        break
    # If the user selects any other integer they are shown the message below and the loop repeats.
    else 
        echo "That is not an option, Please try again"
    fi
done

# End