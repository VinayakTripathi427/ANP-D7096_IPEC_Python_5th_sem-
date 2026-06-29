# Login System with Limited Attempts
#--------------------Problem Statement----------------------
'''
# A system allows only three login attempts.
# The correct username is admin and the password is python123.
# If the credentials are correct, display "Login Successful".
# Otherwise, after three unsuccessful attempts, display "Account Locked".
#
# Sample Input/Output:
# Attempt 1
# Username: admin
# Password: abc
#
# Invalid Credentials
#
# Attempt 2
# Username: admin
# Password: python123
#
# Login Successful
'''
correct_username = "admin"
correct_password = "python123"

#Allow maximum 3 attempts
for attempt in range(1, 4): 
    print(f"Attempt {attempt}")
    
    username = input("Username: ")
    password = input("Password: ")
    
    
    if username == correct_username and password == correct_password:
        print("\nLogin Successful")
        break
    else:
        print("\nInvalid Credentials\n")
else:
    print("Account Locked")
