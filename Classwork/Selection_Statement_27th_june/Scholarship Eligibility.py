#----------------------Scholarship Eligibility--------------------
'''
------------------------------------------------------------------
Problem Statement:

A university provides a scholarship only to students who score 90 or above. 
Write a Python program to accept a student's percentage and determine whether the student is eligible. 
    • If percentage is 90 or above, display: 
        Scholarship Approved 
    • Otherwise display: 
        Scholarship Not Approved 
-----------------------------------------------------------------
-----------------------------------------------------------------
Sample Input 
92

------------------------------------------------------------------
------------------------------------------------------------------
Sample Output 
Scholarship Approved

------------------------------------------------------------------
------------------------------------------------------------------
'''

#-----------------------Coding-------------------------------------
#Input from the Student

Percent = float(input())
if(Percent <= 0 or Percent > 100):
    print("Invalid.")

#Checking Wheather they are eligible for scholarship or not
else:
    if(Percent >= 90):
        print("Scholarship Approved.")
    else:
        print("Scholarship Not Approved.")

#------------------------------------------------------------------
#------------------------------------------------------------------
