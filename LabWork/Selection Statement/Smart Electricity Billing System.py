# -------------------------------------------------
# Problem Statement:
# Electricity bill calculation:
#   0-100 units → ₹5/unit
#   101-300 units → ₹7/unit
#   Above 300 units → ₹10/unit
# Additional Rules:
#   Commercial consumers → 20% extra
#   Bills > ₹5000 → 5% surcharge
#   Senior citizens → 10% discount
#
# Sample Input:
# Units Consumed: 450
# Consumer Type: Commercial
# Senior Citizen (Y/N): Y
#
# Sample Output:
# Base Bill: ₹4500
# Commercial Charge: ₹900
# Surcharge: ₹270
# Senior Citizen Discount: ₹567
# Final Bill Amount: ₹5103
# -------------------------------------------------

units = int(input("Units Consumed: "))
ctype = input("Consumer Type (Residential/Commercial): ")
senior = input("Senior Citizen (Y/N): ")

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100*5) + (units-100)*7
else:
    bill = (100*5) + (200*7) + (units-300)*10

print("Base Bill: ₹", bill)

if ctype == "Commercial":
    extra = 0.20 * bill
    bill += extra
    print("Commercial Charge: ₹", extra)

if bill > 5000:
    surcharge = 0.05 * bill
    bill += surcharge
    print("Surcharge: ₹", surcharge)

if senior == 'Y':
    discount = 0.10 * bill
    bill -= discount
    print("Senior Citizen Discount: ₹", discount)

print("Final Bill Amount: ₹", bill)
