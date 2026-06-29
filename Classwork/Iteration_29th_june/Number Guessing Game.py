#-----------------Number Guessing Game----------------
'''
------------------------------------------------------
Problem Statement 
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.

-------------------------------------------------------
'''
#------------Coding--------------

secret_num = 37

#Displaying output
for i in range(10000):
    attempt = int(input("Guess a number: "))
    if attempt < secret_num:
        print("Number is too low.")
        print("-----------------------")
    elif attempt > secret_num:
        print("Number is too high")
        print("-----------------------")
    else:
        print("Correct")
        break
