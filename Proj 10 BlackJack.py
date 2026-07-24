import blackjack_art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "User Lost, Computer ahs a Blackjack"
    elif u_score == 0:
        return "User Wins with a Blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Computer went over, you Win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You Lose"

def blackjack():
    user_cards= []
    comp_cards= []
    comp_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over :
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computers's First Card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)
    print(f"Your Final Hand: {user_cards}, final score: {user_score} ")
    print(f"Computer's Final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input('Do you want to play a game of BlackJack? Type "y" or "n": ') == "y":
    print("\n" * 30)
    print(blackjack_art.logo)
    blackjack()



