# Scenario: A party organizer wants to distribute pizza slices equally among children. 
# Problem Statement: Write a Python program to find how many slices remain after equal distribution. 

# Input: Total Pizza Slices and Number of Children
total_slices = int(input("Enter Total Pizza Slices: "))
children = int(input("Enter Number of Children: "))

# Calculate Remaining Slices after equal distribution
remaining_slices = total_slices % children

# Output: Remaining Slices
print("Remaining Slices:", remaining_slices)
