print("Welcome to Hangman\n")

word = list("computing")
guessed_word = list("__________")
lives = 5
wordGuessed = False 

while lives>=1 and not wordGuessed :

    print(" ".join(guessed_word))

    user_guess = input("guess a letter/word!(" + str(lives) + \n "lives remaining )\n")