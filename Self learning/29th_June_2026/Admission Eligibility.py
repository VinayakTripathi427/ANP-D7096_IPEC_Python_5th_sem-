# Program to create a list of marks of 50 students with their names
# Display names of students eligible for admission (Marks > 75)

names = []       # List to store student names
marks = []       # List to store marks
eligible = []    # List to store eligible students

for i in range(50):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    
    names.append(name)
    marks.append(mark)
    
    # Check admission eligibility
    if mark > 75:
        eligible.append(name)

# Display eligible students
print("\nStudents eligible for admission:")
print(*eligible)
