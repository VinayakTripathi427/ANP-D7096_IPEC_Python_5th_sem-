# -------------------------------------------------
# Problem Statement:
# Employee evaluated using Project Score, Attendance, Client Feedback.
# Rules:
#   Excellent → All scores > 90
#   Good → Scores > 75
#   Average → Scores > 60
#   Poor → Otherwise
# Additional Rule:
#   Attendance < 70% → Max rating = Average
#
# Sample Input:
# Project Score: 95
# Attendance: 65
# Client Feedback: 92
#
# Sample Output:
# Performance Rating: Average
# Reason: Attendance below 70%
# -------------------------------------------------

project = int(input("Project Score: "))
attendance = int(input("Attendance: "))
feedback = int(input("Client Feedback: "))

if attendance < 70:
    if project > 90 and feedback > 90:
        rating = "Average"
        reason = "Attendance below 70%"
    elif project > 75 and feedback > 75:
        rating = "Average"
        reason = "Attendance below 70%"
    else:
        rating = "Poor"
        reason = "Attendance below 70%"
else:
    if project > 90 and feedback > 90:
        rating = "Excellent"
    elif project > 75 and feedback > 75:
        rating = "Good"
    elif project > 60 and feedback > 60:
        rating = "Average"
    else:
        rating = "Poor"
    reason = "Criteria satisfied"

print("Performance Rating:", rating)
print("Reason:", reason)
