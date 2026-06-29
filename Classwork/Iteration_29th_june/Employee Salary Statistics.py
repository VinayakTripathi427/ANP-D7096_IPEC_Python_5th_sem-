#----------------------- Employee Salary Statistics--------------------------
'''
Problem Statement:
A company has N employees.
Accept the salary of each employee and determine:
• Highest salary
• Lowest salary
• Average salary
• Number of employees earning more than ₹50,000
'''


#Input number of employees
N = int(input("Enter number of employees: "))

#Initialize variables

total_salary = 0            
highest_salary = 0          
lowest_salary = None        
count_above_50000 = 0   


for i in range(N):
    salary = int(input(f"Enter salary of Employee {i+1}: "))
    
    total_salary += salary

    if salary > highest_salary:
        highest_salary = salary
    if lowest_salary is None or salary < lowest_salary:
        lowest_salary = salary
    

    if salary > 50000:
        count_above_50000 += 1


average_salary = total_salary / N


print("\nEmployee Salary Report")
print("Highest salary:", highest_salary)                  
print("Lowest salary:", lowest_salary)                    
print("Average salary:", average_salary)                  
print("Employees earning more than ₹50,000:", count_above_50000)
