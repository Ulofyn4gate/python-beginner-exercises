#Ask the user for a number. Depending on whether the number is 
# even or odd, print out an appropriate message to the user

num = int(input("Enter a number of your choice: "))
if num % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

num1 = int(input("Enter another number: "))
if num1 % 4 == 0:
    print("This number is a multiple of 4")
else:
    print ("This is not a multiple of 4")

num2 = int(input("Enter a new number: "))
check = int(input("Enter a second number: "))
if num2 % check == 0:
    print("The number", check, "can perfectly divde", num2)
else:
    print("There is no perfect division")
    