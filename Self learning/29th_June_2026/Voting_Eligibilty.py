# Program to take ages of 10 people and count how many are eligible for voting

ages = []          # List to store ages
eligible_count = 0 # Counter for eligible voters

for i in range(10):
    age = int(input("Enter age: "))
    ages.append(age)
    
    # Check voting eligibility
    if age >= 18:
        eligible_count += 1

# Display total eligible people
print("\nTotal number of eligible voters:", eligible_count)
