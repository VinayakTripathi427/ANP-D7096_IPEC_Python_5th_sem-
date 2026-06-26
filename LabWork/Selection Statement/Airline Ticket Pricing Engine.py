#--------------Airline Ticket Pricing Engine-------------
'''
---------------------------------------------------------
---------------------------------------------------------
Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000

Additional Charges: 
• Business Class → +₹3000 
• Window Seat → +₹500 
• Weekend Travel → +₹1000 
Discounts: 
• Age below 12 → 50% 
• Age above 60 → 20% 
Calculate the final ticket fare.

-----------------------------------------------------------
-----------------------------------------------------------
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y

------------------------------------------------------------
-----------------------------------------------------------
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0

'''
#------------------------------------------------------------

# Base fare for all tickets
base_fare = 5000

# Taking inputs
age = int(input("Enter Passenger Age: "))
business = input("Business Class (Y/N): ")
window = input("Window Seat (Y/N): ")
weekend = input("Weekend Travel (Y/N): ")

# Calculate additional charges
charges = 0
if business == 'Y':   # Business class adds ₹3000
    charges += 3000
if window == 'Y':     # Window seat adds ₹500
    charges += 500
if weekend == 'Y':    # Weekend travel adds ₹1000
    charges += 1000

print("Base Fare: ₹", base_fare)
print("Additional Charges: ₹", charges)

# Total fare before discount
fare = base_fare + charges

# Apply discounts based on age
if age < 12:          # Children get 50% discount
    fare *= 0.5
    print("Child Discount: 50%")
elif age > 60:        # Senior citizens get 20% discount
    fare *= 0.8
    print("Senior Citizen Discount: 20%")

print("Final Ticket Fare: ₹", fare)
