#This exercise is character input, I am creating a program that asks users their name and afe
#print message addressed to them that tells them the year that they will turn 100 years old.

print("Tell me your name")
name = input()
print ('Your name is ' + name)

print("Tell me your age")
age = int(input())
print("You are ", age, "years old")
year100 = 2026 - age + 100
print ("In ", year100, ' you will be turning 100 years')

print("Write any number of your choice, it could be just a random number")         
anyNum= int(input())
message= f"In {year100} you will be turning 100 years"

print((message + "\n") * anyNum)
