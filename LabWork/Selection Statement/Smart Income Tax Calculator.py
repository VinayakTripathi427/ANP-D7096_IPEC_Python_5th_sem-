#-------------------Smart Income Tax Calculator----------------
'''
Problem Statement:A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax 
• ₹5,00,001 to ₹10,00,000 → 10% 
• ₹10,00,001 to ₹20,00,000 → 20% 
• Above ₹20,00,000 → 30% 

---------------------------------------------------------------
---------------------------------------------------------------
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax. 
• Women taxpayers receive an additional 2% rebate on tax.

--------------------------------------------------------------
--------------------------------------------------------------
Write a Python program to calculate the final tax amount payable.

Sample Input:
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F

---------------------------------------------------------------
---------------------------------------------------------------
Sample Output:
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0
'''

#--------------------------------------------------------------
#-----------------------Coding---------------------------------


# Taking Input from user
Annual_Income = int(input("Enter Annual Income: "))
Age = int(input("Enter Age: "))
Gender = input("Enter Gender (M/F): ").strip().upper()

# Tax Calculation
if Annual_Income <= 500000:
    print("No Tax")

else:
    # Base Tax according to slabs
    if Annual_Income <= 1000000:
        tax = 0.10 * Annual_Income
    elif Annual_Income <= 2000000:
        tax = 0.20 * Annual_Income
    else:
        tax = 0.30 * Annual_Income

    print("Tax before rebate: ₹", tax)

    # Rebates
    senior_rebate = 0
    women_rebate = 0

    if Age >= 60:
        senior_rebate = 0.05 * tax
        print("Senior Citizen Rebate: ₹", senior_rebate)

    if Gender == 'F':
        women_rebate = 0.02 * tax
        print("Women Rebate: ₹", women_rebate)

    # Final Tax
    final_tax = tax - (senior_rebate + women_rebate)
    print("Final Tax Payable: ₹", final_tax)



    
    
        
    

