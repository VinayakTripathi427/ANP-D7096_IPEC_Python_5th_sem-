# Scenario: A school wants to arrange students into equal rows. 
# Problem Statement: Write a Python program to determine how many complete rows can be formed. 

#Input: Total Students and Students per Row
total_students = int(input("Enter Total Students: "))
students_per_row = int(input("Enter Students per Row: "))

#Calculate Number of Complete Rows
complete_rows = total_students // students_per_row

#Output: Number of Complete Rows
print("Number of Complete Rows:", complete_rows)
