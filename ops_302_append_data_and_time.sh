#!/bin/bash

# Script Name:                  Ops 301d8 Challenge 02
# Author:                       David Prutch
# Date of latest revision:      05/31/2023
# Purpose:                      Copy system log to current working directory and append date and time to file name

# Declaration of variables

# Declaration of functions


# Main
###############
# less displays content of a file - syslog file in this case.
# > writes ouput to file.
# "syslog_$(date +%Y_%d_%m_%T)".txt creates file in current working directory with the current date and time appended in the file name.
###############
less /var/log/syslog > "syslog_$(date +%Y_%d_%m_%T)".txt


# End