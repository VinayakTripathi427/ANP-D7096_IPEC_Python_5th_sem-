# Scenario: An e-commerce website offers a fixed discount on products. 
# Problem Statement: Write a Python program to calculate the final payable amount after applying the discount.

# Input: Product Price and Discount Amount
product_price = float(input("Enter Product Price: "))
discount = float(input("Enter Discount Amount: "))

# Calculate Final Price
final_price = product_price - discount

# Output: Final Price
print("Final Price:", final_price)
