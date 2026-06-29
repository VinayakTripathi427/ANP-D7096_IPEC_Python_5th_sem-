#---------------------- Bank Transaction Summary ---------------------
'''
----------------------------------------------------------------------
Problem Statement 
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish. 
Display: 
• Total Deposit 


• Total Withdrawal 
• Final Balance
-----------------------------------------------------------------------
'''
#----------------------------------------------------------------------
#transaction_amt = float(input("Enter transaction amounts: "))
final_balance = 0
total_deposit = 0
total_Withdrawal = 0
for i in range(1000000):
    
    transaction_amt = float(input("Enter transaction amounts: "))
    print("Enter 0 to see your transaction history")
    if transaction_amt > 0:
        final_balance = final_balance + transaction_amt
        total_deposit = total_deposit + transaction_amt
       
    elif transaction_amt < 0:
        final_balance = final_balance - transaction_amt
        total_Withdrawal = total_Withdrawal + transaction_amt
    else:
        print("Final Balance: ",final_balance)
        break

print("Total Deposit: ",total_deposit)
print("Total Withdrawal : ",total_Withdrawal)
print("Final Balance: ",final_balance)


    
