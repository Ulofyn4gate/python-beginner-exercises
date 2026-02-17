#Ask the user for a string and print out whether this 
# string is a palindrome or not

user = str(input("Enter a word: "))
if user == user[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")