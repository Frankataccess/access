import random

def getValue(card):
    try:
        return int(card)
    except:
        if card == "J" or "Q" or "K":
            return 10
        else:
            return 11
        
print("Automatic Blackjack Player\n")

games = 0
gameOver=False

while not gameOver:
    deck = ["A","1","2","3","4","5","6","7","8","9","10","J","K"]
    random.shuffle(deck)

    hand = []
    score = 0

    while score < 17 and len(deck) ! = 0:
        card = deck.pop()
        hand.append(card)
        score = score + getValue(card)

        if score = 21:
            pri
