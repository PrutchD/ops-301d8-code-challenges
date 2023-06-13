#!/usr/bin/env python3

# Script Name:                  Ops 301d8 Challenge 09
# Author:                       David Prutch
# Date of latest revision:      06/09/2023
# Purpose:                      Working with psutil
#                               Requires psutil to be installed
#                               Open Bash terminal run the following command: sudo pip install psutil


# Import libraries
import psutil
# Declaration of variables
user_usage = psutil.cpu_times()
# Declaration of functions

# Main
# Time spent by normal processes executing in user mode
print("User mode process time", user_usage.user)

# Time spent by processes executing in kernel mode
print("Kernel mode process time", user_usage.system)

# Time when system was idle
print("Kernel mode process time", user_usage.system)

# Time spent by priority processes executing in user mode
print("Priority process execution time in user mode", user_usage.nice)

# Time spent waiting for I/O to complete.
print("I/O completion wait time", user_usage.iowait)

# Time spent for servicing hardware interrupts
print("Time servicing hardware interrupts", user_usage.irq)

# Time spent for servicing software interrupts
print("Time servicing software interrupts", user_usage.softirq)

# Time spent by other operating systems running in a virtualized environment
print("Other OSs running in a virtualized environment time", user_usage.steal)

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time running a virtual CPU for guests under control of the Kernel", user_usage.guest)

# End