import random
print("Welcome to Hangman\n\n Please guess the fruit")
word_list = [
    "Apple",
    "Apricot",
    "Avocado",
    "Banana",
    "Blackberry",
    "Blueberry",
    "Cherry",
    "Cranberry",
    "Date",
    "Dragonfruit",
    "Fig",
    "Grape",
    "Grapefruit",
    "Guava",
    "Kiwi",
    "Lemon",
    "Lime",
    "Mango",
    "Melon",
    "Nectarine",
    "Orange",
    "Papaya",
    "Peach",
    "Pear",
    "Pineapple",
    "Plum",
    "Pomegranate",
    "Raspberry",
    "Strawberry",
    "Tangerine",
    "Watermelon"
]
word = random.choice(word_list)
guessed_word = list("________")
lives = 5
wordGuessed = False 

while lives>=1 and not wordGuessed :

    print(" ".join(guessed_word))

    user_guess = input("guess a letter or word: ")

    letter_in_word = False
    for i in range(len(word)):
        if user_guess == word[i]:
            guessed_word[i] = user_guess
            letter_in_word = True 
        

    if letter_in_word == False :
        lives = lives - 1

    if guessed_word == word:
        print(" ".join(guessed_word))
        print("you have guessed the word correctly")
        wordGuessed=True
    elif lives > 1:
        print("you have failed to guess the word correctly :( you have ",lives,"remaining")

    if lives == 0:
        print("game ober the word was",word)