#-------------Secure Vault Access --------------
'''
------------------------------------------------
Problem Statement 
A digital vault can only be opened if the user enters the correct security code. 
Write a Python program that accepts the entered security code. If the entered code is 7890, display:

------------------------------------------------
------------------------------------------------
"Access Granted to the Vault." 
Otherwise, do nothing.

------------------------------------------------
------------------------------------------------
Sample Input 
7890

------------------------------------------------
------------------------------------------------
Sample Output 
Access Granted to the Vault.

************************************************
------------------------------------------------
'''

#--------------------Coding---------------------

#Input from the User

Code = int(input())

#Checking wheather code is correct or not

if(Code == 7890):
    print("Access Granted to the Vault.")
else:
    exit()

