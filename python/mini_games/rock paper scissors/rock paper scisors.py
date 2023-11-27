import random
computer = ""
i = 0
player_wins = 0
computer_wins = 0


dificulty = input("select difficulty: E for easy, N for normal or H for hard: ")
rounds = input("how many rounds would you like to go for: ")
rounds = int(rounds)
dificlty = dificulty.upper()


if dificulty == "E":
    while i < rounds:
        computerChoice = random.randint(0,2)
        choice = input("Enter r for rock, p for paper or s for scissors: ")
        if choice == "r":
            print("The computer chose scissors, You win!")
            i=i+1
            player_wins = player_wins +1
        elif choice == "p":
            print("The computer chose rock, You win!")
            i=i+1
            player_wins = player_wins +1
        else:
            print("The computer chose paper, You win!")
            i=i+1
            player_wins = player_wins +1
    print("you won",player_wins,"times")
elif dificulty == "N":
    while i < rounds:
        computerChoice = random.randint(0,2)
        choice = input("Enter r for rock, p for paper or s for scissors: ")

        if choice == "r":
            if computerChoice == 0:
                print("It's a draw")
                i=i+1
            elif computerChoice == 1:
                print("Computer chose paper you lose")
                computer_wins =computer_wins +1
                i=i+1
            else :
                print("computer chose scissors you win")
                i=i+1

        elif choice == "p":
            if computerChoice == 0 :
                print("computer chose rock you win")
                i=i+1
            elif computerChoice == 1:
                print("Its a draw")
                i=i+1
            elif computerChoice == 2:
                print("computer chose scissors you lose")
                computer_wins =computer_wins +1
                i=i+1
            else:
                print("error")

        elif choice == "s":
            if computerChoice == 0:
                print("computer chose scissors you lsoe")
                computer_wins =computer_wins +1
                i=i+1
            elif computerChoice == 1:
                print("computer chose paper you win")
                i=i+1
            elif computerChoice ==2:
                print("its a draw")
                i=i+1

        else:
           print("error")
       
    
    print("You won ",player_wins," times and lost ",computer_wins)

elif dificulty == "H":
    while i < rounds:
        computerChoice = random.randint(0,2)
        choice = input("Enter r for rock, p for paper or s for scissors: ")
        if choice == "r":
            print("The computer chose paper, You Lose")
            i=i+1
            computer_wins =computer_wins +1
        elif choice == "p":
            print("The computer chose scissors, Lose")
            i=i+1
            computer_wins = computer_wins +1
        elif choice == "s":
            print("The computer chose rock, Lose ")
            i=i+1
            computer_wins = computer_wins +1
    print("you lost",computer_wins,"times")

else:
    print("error")
  

