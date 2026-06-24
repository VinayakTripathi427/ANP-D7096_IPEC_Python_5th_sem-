#Scenario: A company pays an employee a fixed monthly salary and additional incentives based on performance.

# Input: Basic Salary and Incentive
month_salary = float(input("Enter Basic Salary: "))
incentive = float(input("Enter Incentive: "))

# Calculate Total Salary
total_salary = month_salary  + incentive

# Output: Total Salary
print("Total Monthly Salary =", total_salary)
