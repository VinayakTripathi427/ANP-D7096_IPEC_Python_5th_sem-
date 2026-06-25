# Program to calculate Speed

# Input: Distance and Time
distance = float(input("Enter distance (in km): "))
if time <= 0 :
    print("Invalid input! Distance must be non-negative .")
    distance = float(input("Enter distance (in km): "))
time = float(input("Enter time (in hours): "))
if distance < 0:
    print("Invalid input! time must be positive.")
    time = float(input("Enter time (in hours): "))

# Formula: Speed = Distance / Time
speed = distance / time

# Output
print("Speed =", speed, "km/hr")
