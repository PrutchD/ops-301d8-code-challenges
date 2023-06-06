#!/bin/bash

# Script Name:                  Ops 301d8 Challenge 02
# Author:                       David Prutch
# Date of latest revision:      05/31/2023
# Purpose:                      This needs to be run as sudo bash filename to allow erasure of log contents.
#                               Print to the screen the file size of the log files before compression
#                               Compress the contents of the log files listed below to a backup directory with date time stamp in the name.
#                               Clear the contents of the log file
#                               Print to screen the file size of the compressed file
#                               Compare the size of the compressed files to the size of the original log files


# Declaration of variables
# Store file paths in array
file_paths=("var/log/syslog" "var/log/wtmp")
# Declaration of functions


# Main
# Create backup directory
mkdir backup
# Loop through array
for path in "${file_paths[@]}"
do 
    # Display file path
    echo $path
    # Display file size awk '{print $1}' prints only the selected item, prevents repeating path after file size
    echo "File Size"
    file_size=$(wc -c /$path | awk '{print $1}')
    echo $file_size
    # Compress the log file contents to backup directory, includes date and timestamp in file name. -r does this recursively.
    # zip /backup/$path_$(date +%Y_%d_%m_%T).zip /$path
    # # Display compressed file size
    # wc -c /backup/$path_$(date +%Y_%d_%m_%T).zip
    # Display size comparison    
    if [ $path = "var/log/syslog" ]; then
        zip backup/syslog_$(date +%Y_%d_%m_%T).zip /$path 
        echo "Compressing the backup file"
        comp1=$(wc -c backup/syslog_$(date +%Y_%d_%m_%T).zip  | awk '{print $1}')
        echo "Compressed file size $comp1 vs original size $file_size"
    elif [ $path = "var/log/wtmp" ]; then
        zip backup/wtmp_$(date +%Y_%d_%m_%T).zip /$path 
        echo "Compressing the backup file"
        comp2=$(wc -c backup/wtmp_$(date +%Y_%d_%m_%T).zip  | awk '{print $1}')
        echo "Compressed file size $comp2 vs original size $file_size"
    fi
    # Clear contents of log file
    sed -i 'd' /$path
    echo "Original file has been cleared"
    wc -c /$path | awk '{print $1}'
done


# End