import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(0, len(chosen_word)):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters =[]

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if  guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} was not found in the word. You lose a Life")

        if lives == 0:
            print("*********************Game Over*********************")
        print(f"*********************{lives}/6 lives left*********************")

    if "_" not in display:
        game_over = True
        print("*********************You win!*********************")
    print(display)
    print(stages[lives])
