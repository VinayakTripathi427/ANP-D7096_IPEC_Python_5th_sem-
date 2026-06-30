# Program to create a record of 15 persons with name and salary
# Display names of persons eligible for EWS category (Salary ≤ 5 lakh)

names = []      # List to store names
salaries = []   # List to store salaries
ews_list = []   # List to store eligible persons

for i in range(15):
    name = input("Enter name: ")
    salary = float(input("Enter salary (in lakh): "))
    
    names.append(name)
    salaries.append(salary)
    
    # Check EWS eligibility
    if salary <= 5:
        ews_list.append(name)

# Display eligible persons
print("\nPersons eligible for EWS category:")
print(*ews_list)
