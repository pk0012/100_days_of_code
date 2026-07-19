import art
import random
print (art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards= []
comp_cards= []

def blackjack():
    print(art.logo)
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    comp_card1 = random.choice(cards)
    print(f"Your Cards: [{card1}, {card2} ], current score: {card1 + card2}")
    print(f"Computers's First Card: {comp_card1}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == "y":
        card3 = random.choice(cards)
        print(f"[Your Cards: {card1}, {card2}, {card3} ], current score: {card1 + card2 + card3}")






start = input('Do you want to play a game of BlackJack? Type "y" or "n": ')
if start == 'y':
    gamestart = True
    blackjack()
else:
    gamestart = False



