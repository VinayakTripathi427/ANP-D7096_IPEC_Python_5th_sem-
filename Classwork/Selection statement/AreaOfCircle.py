#Write a program to calculate area of circle and validate it
#Taking input from the user 
r = float(input("Enter the Radius os the circle (in cm): "))
if r<0:
    print("Radius cannot be negative.")
    r = float(input("Enter the Radius os the circle (in cm): "))
# Formula: Area = π * r^2

area = 3.14159 *r*r

#output 
print("Area of circle: ",area) 
