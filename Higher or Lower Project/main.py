import art
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description}, from {account_country}"

def check_answer(guess, a_followers_count, b_followers_count):
    if a_followers_count > b_followers_count:
        return guess == "a"
    else:
        return guess == "b"

print(art.logo)
user_score = 0
game_continue = True
item_b = random.choice(data)

while game_continue:
    item_a = item_b
    item_b = random.choice(data)
    if item_a == item_b:
        item_b = random.choice(data)

    print(f"Compare A: {format_data(item_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(item_b)}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)

    a_followers = item_a["follower_count"]
    b_followers = item_b["follower_count"]

    is_correct = check_answer(user_guess, a_followers, b_followers)

    if is_correct:
        user_score += 1
        print(f"You're right!, Your score is {user_score}.")
    else:
        print(f"Sorry, you're wrong. Your score is {user_score}.")
        game_continue = False
