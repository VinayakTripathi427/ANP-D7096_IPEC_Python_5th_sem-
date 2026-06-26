#---------Problem---------
'''
--------------------------
A bank evaluates loan applications using: 
• Credit Score ≥ 750 
• Annual Income ≥ ₹8,00,000 
• Existing Loan Amount ≤ ₹2,00,000

--------------------------
--------------------------
Conditions: 
• All conditions satisfied → Approved 
• Only one condition fails → Manual Review

--------------------------
--------------------------
'''

credit_score = int(input("Enter Credit Score: "))
income = float(input("Enter Annual Income: "))
loan_amount = float(input("Enter Existing Loan Amount: "))

fails = 0
reason = []

if credit_score < 750:
    fails += 1
    reason.append("Credit Score criteria not satisfied.")
if income < 800000:
    fails += 1
    reason.append("Income criteria not satisfied.")
if loan_amount > 200000:
    fails += 1
    reason.append("Existing Loan criteria not satisfied.")

if fails == 0:
    print("Loan Status: Approved")
elif fails == 1:
    print("Loan Status: Manual Review")
    print("Reason:", reason[0])
else:
    print("Loan Status: Rejected")
    print("Reasons:", ", ".join(reason))
