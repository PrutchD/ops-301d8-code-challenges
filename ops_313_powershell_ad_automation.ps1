# Script Name:                  Ops 301d8 Challenge 13
# Author:                       David Prutch
# Date of latest revision:      06/15/2023
# Purpose:                      Powershell automation script to create new user in Active Directory (AD)

# Declaration of variables

# Declaration of functions


# Main
# Uses the New-ADUser command with all of the following parameters to create a nuew user in active directory.
# Account password requests input from the person running the script to create secure password.
New-ADUser `
-Name "Franz Ferdinand" `
-GivenName "Franz" `
-Surname "Ferdinand" `
-SamAccountName "f.ferdinand" `
-AccountPassword (Read-Host _AsSecureString "Input User Password") `
-ChangePasswordAtLogon $True `
-Title "TPS Reporting Lead" `
-Department "TPS Department" `
-Company "Globex USA" `
-City "Springfield" `
-State "OR" `
-Country "US" `
-PostalCode "97475" `
-EmailAddress "ferdi@GlobeXpower.com" `
-Enabled $True

# End