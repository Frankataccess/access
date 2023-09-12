import random 
rand_num=random.randint(0,100)
while True:
    guess = int(input("guess the number between 1 and 100 : "))
    if guess > rand_num:
        print("my number is lower than",guess)
    elif guess < rand_num:
        print("my number is higher than",guess)
    else :
        print("you guessed my number")
        exit()
