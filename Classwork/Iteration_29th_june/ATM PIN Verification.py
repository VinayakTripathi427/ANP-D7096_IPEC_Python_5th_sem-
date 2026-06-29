#------------ATM PIN Verification------------------
'''
Problem Statement 
An ATM allows a user to enter the correct PIN.
The correct PIN is 4589. The user can keep entering the 
PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. 
Sample Output 
Enter PIN: 1234 
Incorrect PIN 

----------------------------------------------------
Enter PIN: 9876 
Incorrect PIN 

-----------------------------------------------------
Enter PIN: 4589 
Access Granted

-----------------------------------------------------
'''
#-------------------Coding---------------------------
CORRECT_PIN = 4589
i = 1000000000000000
while i>0:
    pin = int(input("Enter PIN: "))
    
    if pin == CORRECT_PIN:
        print("Access Granted")
        break   
    else:
        print("Incorrect PIN\n")
    i=i-1
#-----------------------------------------------------

