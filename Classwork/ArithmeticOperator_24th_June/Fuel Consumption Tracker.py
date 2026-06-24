#Scenario: A person wants to calculate the average fuel consumption of a car. 
#Problem Statement: Write a Python program to find the average mileage of a car.

#Input
TDT = float(input("Total distance traveled (km): "))
FC = float(input("Fuel consumed (liters): "))

#Output
Mil = TDT/FC

print("Mileage (km/l): ",Mil)
