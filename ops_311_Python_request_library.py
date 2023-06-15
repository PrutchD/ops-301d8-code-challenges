#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 11
# Author:                       David Prutch
# Date of latest revision:      06/14/2023
# Purpose:                      Working with Python Request Library


# Import libraries
import requests
# Declaration of variables
url_inp = input("Enter the destination url in the form https://www.domain-name.com: ")
request_type = ["1: GET", "2: POST", '3: PUT', "4: DELETE", "5: HEAD", "6: PATCH", "7: OPTIONS"] 
choice = ""
response = ""
# Declaration of functions
def menu():
    for req in request_type:
        print(req)

def menu_selection(var):
    var = int(var)
    global choice
    if var == 1:
        choice = input("would you like to send the following request: requests.get(" + url_inp + ")? y/n: ")   
    elif var == 2:
        choice = input("would you like to send the following request: requests.post(" + url_inp + ")? y/n: ")
    elif var == 3:
        choice = input("would you like to send the following request: requests.put(" + url_inp + ")? y/n: ")
    elif var == 4:
        choice = input("would you like to send the following request: requests.delete(" + url_inp + ")? y/n: ")
    elif var == 5:
        choice = input("would you like to send the following request: requests.head(" + url_inp + ")? y/n: ")
    elif var == 6:
        choice = input("would you like to send the following request: requests.patch(" + url_inp + ")? y/n: ")
    elif var == 7:
        choice = input("would you like to send the following request: requests.options(" + url_inp + ")? y/n: ")
    else:
        print("That was not a choice from the menu")

def run_request(menu_inp, selection):
    global response
    menu_inp = int(menu_inp)
    if selection == "y" and menu_inp == 1:
        response = requests.get(url_inp)
        print(response.status_code)
    elif selection == "y" and menu_inp == 2:
        response = requests.post(url_inp)
        print(response.status_code)
    elif selection == "y" and menu_inp == 3:
        response = requests.put(url_inp)
        print(response.status_code)
    elif selection == "y" and menu_inp == 4:
        response = requests.delete(url_inp)
        print(response.status_code)
    elif selection == "y" and menu_inp == 5:
        response = requests.head(url_inp)
        print(response.status_code)
    elif selection == "y" and menu_inp == 6:
        response = requests.patch(url_inp)
        print(response.status_code)        
    elif selection == "y" and menu_inp == 7:
        response = requests.options(url_inp)
        print(response.status_code)
    else:
        print("That's ok, I didn't want to run that for you anyway :(")

def error_messages(var):
    if str(response.status_code) == "200":
        print("Success")
        print(response.headers)
    elif str(response.status_code) == "400":
        print("Bad Request")
        print(response.headers)
    elif str(response.status_code) == "401":
        print("Unauthorized")
        print(response.headers)
    elif str(response.status_code) == "402":
        print("Payment Required")
        print(response.headers)
    elif str(response.status_code) == "403":
        print("Forbidden")
        print(response.headers)
    elif str(response.status_code) == "404":
        print("Not Found")
        print(response.headers)
    elif str(response.status_code) == "405":
        print("Method Not Allowed")
        print(response.headers)
    elif str(response.status_code) == "400":
        print("Request Timeout")
        print(response.headers)
    else:
            print("This is not a common header, I do not have it programmed in, sorry")
    
# Main
menu()
inp = input("Please select a number from the menu: ")
menu_selection(inp)
run_request(inp, choice)
error_messages(response)



# End