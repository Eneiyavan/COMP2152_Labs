import random
choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print ("Error: The input should be an interger between 1and 3!")
else:
    # Determine the winner logic using if/elif/else
    computerChoice = random.randint(1,3)
    
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Sciccors - You Win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You Win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Sciccors beats Rock - You Win!")
    else: 
        print("You lose!")