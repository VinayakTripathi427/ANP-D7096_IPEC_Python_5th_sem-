# Program to calculate Area and Perimeter of Rectangle

# Input: Length and Breadth of rectangle
length = float(input("Enter length of rectangle: "))
if length <= 0 or breadth <= 0:
    print("Invalid input! Length numbers.")
    length = float(input("Enter length of rectangle: "))

breath = float(input("Enter breath of rectangle: "))
if length <= 0 or breadth <= 0:
    print("Invalid input! breadth must be positive numbers.")

# Formula: Area = length × breadth
area = length * breadth

# Formula: Perimeter = 2 × (length + breadth)
perimeter = 2 * (length + breadth)

# Output
print(" Area of rectangle =", area)
print(" Perimeter of rectangle =", perimeter)

