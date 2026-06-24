#Scenario: A customer withdraws money from their bank account. 
#Problem Statement: Write a Python program to calculate the remaining balance after withdrawal.

# Input: Current Balance and Withdrawal Amount
current_balance = float(input("Enter Current Balance: "))
withdrawal_amount = float(input("Enter Withdrawal Amount: "))

# Calculate Remaining Balance
remaining_balance = current_balance - withdrawal_amount

# Output: Remaining Balance
print("Remaining Balance:", remaining_balance)
