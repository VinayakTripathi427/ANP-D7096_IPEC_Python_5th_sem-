# -------------------------------------------------
# Problem Statement:
# Student appears in 5 subjects.
# Rules:
#   Minimum 40 marks in each subject → Pass
#   Distinction → Average ≥ 75
#   First Division → Average ≥ 60
#   Second Division → Average ≥ 50
#   Pass → Average ≥ 40
#   Fail → Any subject < 40
#
# Sample Input:
# Hindi: 85
# English: 78
# Mathematics: 82
# Science: 75
# Computer: 90
#
# Sample Output:
# Average Marks: 82.0
# Result: PASS
# Classification: Distinction
# -------------------------------------------------

marks = []
subjects = ["Hindi", "English", "Mathematics", "Science", "Computer"]

for sub in subjects:
    marks.append(int(input(f"{sub}: ")))

if min(marks) < 40:
    print("Result: FAIL")
else:
    avg = sum(marks)/5
    print("Average Marks:", avg)
    print("Result: PASS")
    if avg >= 75:
        print("Classification: Distinction")
    elif avg >= 60:
        print("Classification: First Division")
    elif avg >= 50:
        print("Classification: Second Division")
    else:
        print("Classification: Pass")
