#---------------------Parking Entry Validation---------------------
'''
Problem Statement :
    Only vehicles having a valid parking pass are allowed to enter a private parking area. 
    Accept either 1 (Valid Pass) or 0 (No Pass). 
        • If the input is 1, display: 
                        Entry Allowed 
        • Otherwise display: 
                        Entry Denied
------------------------------------------------------------------
Sample Input 
0
------------------------------------------------------------------
Sample Output 
Entry Denied
------------------------------------------------------------------
'''
#---------------------Coding----------------------

#Input From User

Passs = int(input())


if(Passs == 0 or Passs == 1):
    if(Passs == 0):
        print("Entry Denied.")
    else:
        print("Entry Allowed.")
else:
    print("Please Enter valid input.")

#---------------------------------------------------
