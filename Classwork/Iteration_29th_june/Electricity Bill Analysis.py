#----------------Electricity Bill Analysis-----------------
'''
Problem Statement 
An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
• Total units consumed 
• Average units consumed 
• Highest consumption 
• Lowest consumption
'''

#------------Coding-----------------

#Input number of houses
N = int(input("Enter number of houses: "))

# Initialize variables
total_units = 0         
highest_units = 0        
lowest_units = None      

#Loop through each house to take input
for i in range(N):
    units = int(input(f"Enter units consumed by House {i+1}: "))
    
  
    total_units += units
    

    if units > highest_units:
        highest_units = units
    

    if lowest_units is None or units < lowest_units:
        lowest_units = units

# Calculate average
average_units = total_units / N

#Display the report
print("\nElectricity Consumption Report")
print("Total units consumed:", total_units)       # Total units
print("Average units consumed:", average_units)   # Average units
print("Highest consumption:", highest_units)      # Highest units
print("Lowest consumption:", lowest_units)        # Lowest units
