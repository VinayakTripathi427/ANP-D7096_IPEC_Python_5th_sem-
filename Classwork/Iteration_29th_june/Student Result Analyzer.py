#---------------Student Marks Analysis----------------
'''
# Problem Statement:
# A teacher wants to analyze the marks of N students.
# Accept the marks of each student (out of 100).
#
# Finally display:
# • Highest Marks
# • Lowest Marks
# • Average Marks
# • Number of students who passed (Marks ≥ 40)
# • Number of students who scored distinction (Marks ≥ 75)
'''
N = int(input("Enter number of students: "))


total_marks = 0             
highest_marks = 0
lowest_marks = None         
count_pass = 0              
count_distinction = 0        

#Loop through each student to take marks input
for i in range(N):
    marks = int(input(f"Enter marks of Student {i+1}: "))
    
    
    total_marks += marks
    
    
    if marks > highest_marks:
        highest_marks = marks
    
    
    if lowest_marks is None or marks < lowest_marks:
        lowest_marks = marks
    
   
    if marks >= 40:
        count_pass += 1
    
   
    if marks >= 75:
        count_distinction += 1


average_marks = total_marks / N

print("\nStudent Marks Report")
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Number of students who passed:", count_pass)
print("Number of students with distinction:", count_distinction)
