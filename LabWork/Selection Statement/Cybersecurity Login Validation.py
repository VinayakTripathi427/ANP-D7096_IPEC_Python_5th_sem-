# -------------------------------------------------
# Problem Statement:
# Login system validates Username, Password, OTP
# Conditions:
#   All correct → Login Successful
#   Incorrect OTP → Re-enter OTP
#   Incorrect Password after 3 attempts → Account Locked
#   Incorrect Username → User Not Found
#
# Sample Input:
# Username: admin
# Password: admin123
# OTP: 4567
#
# Sample Output:
# Login Successful
# Welcome Admin
# -------------------------------------------------

username = input("Username: ")
password = input("Password: ")
otp = input("OTP: ")

if username != "admin":
    print("User Not Found")
else:
    attempts = 1
    while password != "admin123" and attempts < 3:
        password = input("Re-enter Password: ")
        attempts += 1
    if password != "admin123":
        print("Account Locked")
    else:
        if otp != "4567":
            print("Incorrect OTP. Re-enter OTP")
        else:
            print("Login Successful")
            print("Welcome Admin")
