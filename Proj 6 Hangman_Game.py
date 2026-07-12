import random
word_list = ["aardvark", "baboon", "camel"]


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
        if lives == 0:
            game_over = True
        print(f"You guessed incorrectly! You have {lives}/6 lives left")
    if "_" not in display:
        game_over = True
    print(display)
    print(stages[lives])
