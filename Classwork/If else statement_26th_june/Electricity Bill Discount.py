'''----------- Electricity Bill Discount-----------
---------------------------------------------------
Problem Statement :An electricity provider offers a
10% discount on the total bill amount if the customer's
bill is ₹5,000 
or more. Otherwise, no discount is applied. 
---------------------------------------------------
---------------------------------------------------
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid.
---------------------------------------------------
---------------------------------------------------
Sample Input 1 
Enter the electricity bill amount: 6200
---------------------------------------------------
---------------------------------------------------
Sample Output 1
Discount Applied!
Final Bill Amount: ₹5580.0
---------------------------------------------------
---------------------------------------------------
Sample Input 2 
Enter the electricity bill amount: 4200
---------------------------------------------------
---------------------------------------------------
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200
---------------------------------------------------
---------------------------------------------------'''

#-----Coding-----

#Input from user
Amt = float(input("Enter the Bill Amount (in RS): "))
if(Amt <= 0):
    exit("You don't have to pay anything.")
#Checking condition for discount
if(Amt <= 5000):
    print("No Discount Applied!")
    print("Final Bill Amount: ","₹",Amt)
#Applying Discount
else:
    dis = 0.10*Amt
    Amt = Amt-dis
    print("Discount Applied!")
    print("Final Bill Amount: ₹",Amt)

#-------------------------------------------------
#-------------------------------------------------
#----------------------Output---------------------
'''
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200
'''
    


