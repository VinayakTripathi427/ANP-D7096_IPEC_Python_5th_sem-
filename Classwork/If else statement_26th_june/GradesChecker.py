#-----Problem Statement 3 : Student Grade Calculator -----
'''
A school assigns grades based on the marks obtained by students according to the following criteria: 
• Marks 90 and above → Grade A 
• Marks 75 to 89 → Grade B 
• Marks 50 to 74 → Grade C 
• Below 50 → Grade F 

Write a Python program to accept marks from the user and display the corresponding grade.

#----------------------------------------------------------

Sample Input 
Enter Marks: 92 
Sample Output 
Grade A

#----------------------------------------------------------

Sample Input 
Enter Marks: 80 
Sample Output 
Grade B
#----------------------------------------------------------

Sample Input 
Enter Marks: 65 
Sample Output 
Grade C

#----------------------------------------------------------

Sample Input 
Enter Marks: 35 
Sample Output 
Grade F

#-----------------Coding-----------------------------------'''

#Taking Input from the user
Marks = int(input("Enter Marks: "))
if(Marks <= 0 or Marks > 100):
    print("Invalid Input")
    Marks = int(input("Enter Marks: "))

#Checking Grades
if Marks >= 90:
    print("A")

elif (Marks >= 75 and Marks <= 89):
    print("B")

elif (Marks >= 50 and Marks <= 74):
    print("C")

else:
    print("D")

#----------------------------------------------------------
#----------------------------------------------------------





