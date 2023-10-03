import random

def choose_word():
    word_list = ["python", "hangman", "programming", "developer", "computer", "keyboard", "mouse"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            guessed_letters.append(guess)
            print("Incorrect!")
            attempts -= 1

        print(display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Sorry, you're out of attempts. The word was:", word_to_guess)

hangman()