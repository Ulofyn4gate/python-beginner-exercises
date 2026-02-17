#write a program that returns a list that contains only the 
# elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elems = []

for x in a:
    if x in b and x not in elems:
            elems.append(x,)
print(elems)

#Randomly generate two lists to test this
#Write this in one line of Python 

import random 

a = [random.randint(1, 51) for _ in range(10)]
b = [random.randint(1,51) for _ in range(12)]


print ("List a:", a)
print ("List b:", b)
print(list(set(a) & set (b)))
