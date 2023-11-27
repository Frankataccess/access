import random
def printRules():
    print("The computer will think of either rock,paper or scissors. ")
    print("You will enter r for rock, p for paper or s for scissors")
    print("The computer will reveal its choice and the winner")
print()

def playGame():
    choice=input("enter r for rock, p for paper or s for scissors: ")
    computerChoice = random.randint(0,2)



    if choice == "r":
        if computerChoice == 0:
            print("It's a draw")
        elif computerChoice == 1:
            print("Computer wins")
        else :
            print("player wins")
    elif choice == "p":
        if computerChoice == 0 :
            print("player wins")
        elif computerChoice == 1:
            print("Its a draw")
        elif computerChoice == 2:
            print("Commputer wins")
        else:
            print("error")
    elif choice == "s":
        if computerChoice == 0:
            print("computer wins")
        elif computerChoice == 1:
            print("You win")
        elif computerChoice ==2:
            print("its a draw")
        

print("Welcome to the Rock, Paper, Scissors Game")
playGame()
print("=========================================") 
input("press enter to exit")
