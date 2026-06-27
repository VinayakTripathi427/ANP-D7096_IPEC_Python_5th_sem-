#--------------------Courier Delivery Charge -------------------

'''
Problem Statement: 
    A courier company calculates delivery charges based on the package weight. 
        • Weight up to 2 kg → ₹50 
        • Weight greater than 2 kg and up to 5 kg → ₹100 
        • Weight greater than 5 kg → ₹180
    Write a Python program to display the delivery charge.
    
---------------------------------------------------------------
Sample Input 
4

---------------------------------------------------------------
Sample Output 
Delivery Charge = ₹100

---------------------------------------------------------------
'''

#------------------------Code----------------------------------

#Input From the User

Weight = float(input("Enter Weight (in Kg): "))

#calculating delivery charges based on the package weight

if(Weight <= 0):
    print("Please Enter Valid Weight.")
elif(Weight > 0 and Weight <= 2):
    print("₹50")
elif(Weight > 2 and Weight <= 5):
    print("₹100")
else:
    print("₹180")

#------------------------------------------------------------------
#------------------------------------------------------------------

    
    
    
