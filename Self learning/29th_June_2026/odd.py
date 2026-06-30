# Program to separate odd numbers from input and store all numbers

List = []   # List to store only odd numbers
list1 = []  # List to store all entered numbers

# Loop to take 10 inputs from user
for i in range(10):
    m = int(input())   # Accept integer input from user
    
    # Check if number is odd
    if m % 2 != 0:
        List.append(m)   # Add odd number to List
    
    list1.append(m)      # Add every number to list1

# Print all odd numbers (without brackets, space-separated)
print(*List)

# Print all entered numbers (with brackets, as a list)
print(list1)

