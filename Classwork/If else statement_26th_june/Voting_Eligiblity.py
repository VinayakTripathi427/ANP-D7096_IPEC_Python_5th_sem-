#Program To check Wheather the user is eligible or not to vote.
'''-----------------------------------------------------------
-----------------------------------------------------------'''
#--------------Coding--------------
Age = int(input("Enter Your Age: "))
if(Age <= 0):
    exit("Invalid Input.")
#-----------------------------------------------------------
#-----------------------------------------------------------
#Checking Eligble or not
#if elgible
if(Age >= 18):
    print("You are Eligible to Vote.")
#-----------------------------------------------------------
#-----------------------------------------------------------
#if Not eligible    
else:
    print("You are not Eligible to vote.")


