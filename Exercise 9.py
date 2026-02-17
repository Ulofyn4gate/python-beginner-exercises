#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them 
# whether they guessed too low, too high, or exactly right.

#Keep the game going until the user types “exit”

#Keep track of how many guesses the user has 
# taken, and when the game ends, print this out.

import random


wins = 0
print("Guess a number from 1 to 9")
print(" To quit the game at any time, type 'exit'")

while True:
    rannum = random.randint(1, 9)   # new number each round
    guesses = 0


    while True:
        user = input("Your guess: ").lower()

        #Exit option
        if user == "exit":
            print("Thanks for playing!")
            print("Total rounds won:", wins)
            print("Total guesses:", guesses )
            exit()


        user =int(user)
        guesses += 1 #counts guesses

        if user > rannum:
            print("The number you guessed is too high")
        elif user < rannum:
            print ("The number you guessed is too low")
        elif user == rannum:
            print("You guessed right!")
            wins += 1  
            rannum = random.randint(1,9)




    

    
