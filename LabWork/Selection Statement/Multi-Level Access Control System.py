# -------------------------------------------------
# Problem Statement:
# Assign access levels based on role:
#   Admin + Security Clearance ≥ 5 → Full Access
#   Manager + Experience > 5 Years → Department Access
#   Employee + Experience > 2 Years → Limited Access
#   Guest → Read-Only Access
#   Inactive Account → No Access
#
# Sample Input:
# Role: Admin
# Security Clearance: 6
# Account Status: Active
#
# Sample Output:
# Access Level: FULL ACCESS
# -------------------------------------------------

role = input("Role: ")
status = input("Account Status (Active/Inactive): ")

if status == "Inactive":
    print("Access Level: NO ACCESS")
else:
    if role == "Admin":
        clearance = int(input("Security Clearance: "))
        if clearance >= 5:
            print("Access Level: FULL ACCESS")
        else:
            print("Access Level: Limited Admin Access")
    elif role == "Manager":
        exp = int(input("Experience (Years): "))
        if exp > 5:
            print("Access Level: Department Access")
        else:
            print("Access Level: Limited Access")
    elif role == "Employee":
        exp = int(input("Experience (Years): "))
        if exp > 2:
            print("Access Level: Limited Access")
        else:
            print("Access Level: Basic Access")
    elif role == "Guest":
        print("Access Level: Read-Only Access")
