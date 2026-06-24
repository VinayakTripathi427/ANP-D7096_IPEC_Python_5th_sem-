# Scenario: A person invests money and wants to see how the amount grows over years. 
# Problem Statement: Write a Python program to calculate the value of money after a certain number of years assuming it doubles every year. 

# Input: Initial Amount and Number of Years
initial_amount = float(input("Enter Initial Amount: "))
years = int(input("Enter Number of Years: "))

# Calculate Final Amount (doubles every year)
final_amount = initial_amount * (2 ** years)

# Output: Final Amount
print("Final Amount after", years, "years:", final_amount)
