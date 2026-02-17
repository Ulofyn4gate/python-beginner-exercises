#Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

while True:
    print('\n--- Rock Paper Scissors ---')
    
    P1 = input("Player 1 - Choose Rock, Paper, or Scissors: ").capitalize()
    P2 = input("Player 2 - Choose Rock, Paper, or Scissors: ").capitalize()

    valid = ["Rock", "Paper", "Scissors"]
    if P1 not in valid or P2 not in valid:
        print("Invalid input")
        continue

    if P1 == P2:
        print("it is a tie")
    elif (P1 == "Rock" and P2 == "Scissors") or \
        (P1 == "Scissors" and P2 == "Paper") or \
        (P1 == "Paper" and P2 == "Rock"):
        print("Player 1 wins")
    
    elif (P2 == "Rock" and P1 == "Scissors") or \
        (P2 == "Scissors" and P1 == "Paper") or \
        (P2 == "Paper" and P1 == "Rock"):
        print("Player 2 wins")

    

    again = input("Do you want to go another round? (yes/no): ").lower()
    if again == "no":
        print ("Thanks for playing")
        break






    



