''' Program to find out greatest Number between two number. '''
#Input of first number from user
num1 = int(input("Enter first number: "))
#----------------------------------------

#Input of Second Number
num2 = int(input("Enter Second number: "))
#-----------------------------------------

print("-----------------------------------")

#Finding th greatest
if(num1 > num2):
    print(num1,"is greater than",num2)
elif(num2 > num1):
    print(num2,"is greater than",num1)
else:
    print(num1,"and",num2,"Both are equal")

#----------------------------------------


    
