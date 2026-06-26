# -------------------------------------------------
# Problem Statement:
# Scholarship awarded based on percentage:
#   95+ → 100%
#   90-94 → 75%
#   85-89 → 50%
#   80-84 → 25%
#   Below 80 → No Scholarship
# Conditions:
#   Family income < ₹8,00,000
#   No disciplinary action
#
# Sample Input:
# Percentage: 92
# Family Income: 500000
# Disciplinary Action (Y/N): N
#
# Sample Output:
# Scholarship Awarded: 75%
# -------------------------------------------------

percentage = int(input("Percentage: "))
income = float(input("Family Income: "))
disciplinary = input("Disciplinary Action (Y/N): ")

if disciplinary == 'Y' or income >= 800000:
    print("Scholarship Awarded: No Scholarship")
else:
    if percentage >= 95:
        print("Scholarship Awarded: 100%")
    elif percentage >= 90:
        print("Scholarship Awarded: 75%")
    elif percentage >= 85:
        print("Scholarship Awarded: 50%")
    elif percentage >= 80:
        print("Scholarship Awarded: 25%")
    else:
        print("Scholarship Awarded: No Scholarship")
