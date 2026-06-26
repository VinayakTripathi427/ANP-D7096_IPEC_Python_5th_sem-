# -------------------------------------------------
# Problem Statement:
# Hospital prioritizes patients based on:
#   Critical Condition → Immediate Treatment
#   Oxygen < 90 → High Priority
#   Age > 65 → Medium Priority
#   Others → Normal Priority
#
# Sample Input:
# Critical Condition (Y/N): N
# Age: 70
# Oxygen Level: 94
#
# Sample Output:
# Patient Priority: Medium Priority
# Reason: Senior Citizen
# -------------------------------------------------

critical = input("Critical Condition (Y/N): ")
age = int(input("Age: "))
oxygen = int(input("Oxygen Level: "))

if critical == 'Y':
    print("Patient Priority: Immediate Treatment")
elif oxygen < 90:
    print("Patient Priority: High Priority")
elif age > 65:
    print("Patient Priority: Medium Priority")
    print("Reason: Senior Citizen")
else:
    print("Patient Priority: Normal Priority")
