#Scenario: A customer purchases multiple packets of rice from a grocery store. 

#Problem Statement: Write a Python program to calculate the total cost of rice packets purchased. 

#Input
Price_per_Packet = float(input("Enter price per packet: "))
Number_of_packet = float(input("Enter Number of packets: "))

#Calculation
Total_price = Price_per_Packet*Number_of_packet

#Output
print("Total(in Rs): ",Total_price)
