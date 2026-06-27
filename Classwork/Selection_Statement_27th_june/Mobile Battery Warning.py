#------------------Mobile Battery Warning -------------------
'''
Problem Statement:
    A smartphone displays a low battery warning only when the battery percentage falls below 15%.
    
    Write a Python program to accept the battery percentage. 
        If the battery is below 15, display: 
        Connect Charger Immediately 
        Otherwise, display nothing.

--------------------------------------------------------------
Sample Input 
10
--------------------------------------------------------------
Sample Output 
Connect Charger Immediately
--------------------------------------------------------------
'''
#---------Coding------------

#Input From User
battery_percentage = int(input("Enter battery Percentage: "))

#Validating Data
if(battery_percentage < 0 or battery_percentage > 100):
    exit("Invalid Data")

#Displaying Mobile Battery Warning
if(battery_percentage < 15):
    print("Connect Charger Immediately.")
#------------------------------------------------------------
#------------------------------------------------------------
'''
---------------Output-------------------------
Enter battery Percentage: 101
Invalid Data
-----------------------------------------------
'''
