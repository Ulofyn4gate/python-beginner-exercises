#Create a program that asks the user for a number and then prints out 
# a list of all the divisors of that number

user = int(input("Enter a number: "))
div = []

for x in range (1,user + 1):
    if user % x == 0:
        div.append(x)

print("The Divisors are:", div)
   
