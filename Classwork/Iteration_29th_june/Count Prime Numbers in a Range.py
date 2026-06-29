#------Count Prime Numbers in a Range----------------

'''Problem Statement 
Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime numbers 
found.
'''


start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

prime_count = 0

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:   # prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            prime_count += 1

print("\nTotal Prime Numbers Found:", prime_count)
