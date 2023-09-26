import random
computer = ""
i = 0
player_wins = 0
computer_wins = 0
def printRules():
    print("The computer will think of either rock,paper or scissors. ")
    print("You will enter r for rock, p for paper or s for scissors")
    print("The computer will reveal its choice and the winner")
print()

dificulty = input("select difficulty: E for easy, N for normal or H for hard: ")
rounds = input("how many rounds would you like to go for: ")
rounds = int(rounds)
dificlty = dificulty.upper
choice = input("Enter r for rock, p for paper or s for scissors: ")
choice = choice.lower
if dificulty == "E":
    while i < rounds:
        if choice == "r":
         print("The computer chose scissors, You win!")
         player_wins = player_wins +1
        elif choice == "p":
            print("The computer chose rock, You win!")
            player_wins = player_wins +1
        else:
         print("The computer chose paper, You win!")
         player_wins = player_wins +1
    print("you won",player_wins,"times")
elif dificulty == "N":
    while i < rounds:
        computerChoice=random.randint(0,2)
        if computerChoice == 0:
            computer =="r"
        elif computerChoice == 1:
            computer == "p"
        else:
            computer == "s"

        if computer == choice:
            print("draw")
        elif computer == "r" and choice =="p":
            print("The computer chose rock, You win!") 
            player_wins = player_wins +1
        elif computer == "p" and choice =="s":
            print("The computer chose paper, You win!") 
            player_wins = player_wins +1
        elif computer == "s" and choice =="r":
            print("The computer chose rock, You win!") 
            player_wins = player_wins +1
        elif computer == "p" and choice =="r":
            print("The computer chose paper, You Lose") 
            computer_wins = computer_wins +1
        elif computer == "s" and choice =="p":
            print("The computer chose scissors, You Lose") 
            computer_wins = computer_wins +1
        elif computer == "r" and choice =="s":
            print("The computer chose rock, You Lose") 
            computer_wins = computer_wins +1
        else:
            print("error")
    
    print("You won ",player_wins," times and lost ",computer_wins)

elif dificulty == "H":
    while i < rounds:
        if choice == "r":
         print("The computer chose paper, You Lose")
         computer_wins =computer_wins +1
        elif choice == "p":
            print("The computer chose scissors, Lose")
            computer_wins = computer_wins +1
        elif choice == "s":
         print("The computer chose rock, Lose ")
         computer_wins = computer_wins +1
    print("you lost",computer_wins,"times")