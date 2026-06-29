# -------------------Shopping Cart Billing System ----------------------
'''
Problem Statement:
# A supermarket allows a customer to purchase multiple products.
# The customer first enters the number of products.
# For each product, enter:
# • Product Name
# • Quantity
# • Price per Unit
#
# Finally display:
# • Individual Product Cost
# • Total Bill Amount
# • Most Expensive Product
# • Cheapest Product
# • Average Product
'''
N = int(input("Enter number of products: "))
products = []              
total_bill = 0             
highest_cost = 0           
lowest_cost = None         
most_expensive = ""        
cheapest = ""              

for i in range(N):
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = int(input("Enter Price per Unit: "))
    
    cost = qty * price
    products.append((name, cost))   
    
    total_bill += cost
    
    if cost > highest_cost:
        highest_cost = cost
        most_expensive = name
    
    
    if lowest_cost is None or cost < lowest_cost:
        lowest_cost = cost
        cheapest = name


average_cost = total_bill / N


print("\nProduct Costs:")
for name, cost in products:
    print(name, "->", cost)

print("\nTotal Bill Amount:", total_bill)
print("Most Expensive Product:", most_expensive, f"({highest_cost})")
print("Cheapest Product:", cheapest, f"({lowest_cost})")
print("Average Product Cost:", average_cost)
