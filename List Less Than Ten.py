# write a program that prints out all the elements 
# of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        print (x)

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 
# from this list in it and print out this new list.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for x in a:
    if x < 5:
        newlist.append(x)
print (newlist)

#Write this in one line of Python.
newlist = [x for x in a if x < 5]
print(newlist)

#Ask the user for a number and return a list that contains only elements from the original list a 
# that are smaller than that number given by the user

num = int(input(" Hello User, Enter a number: "))
userList = [x for x in a if x < num]
if not userList: #f nothing matches, print: "No numbers found"
    print("No numbers found")
else: 
    print(userList)


