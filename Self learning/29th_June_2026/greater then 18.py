#Initialising blanck list 
people = []
list = []
count = 0
for i in range(15):
    #Taking input from user
    age = int(input())
    if age >=18:
        list.append(age)
        #Number of persons older than 18 years
        count = count+1
    people.append(age)
#Displaying Total people
print(people)
print(list)
#Displaying number of Adults
print(count)
