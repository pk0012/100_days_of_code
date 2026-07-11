import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock, paper , scissors]
print ("Welcome to Rock paper scissors!")
choice_u = int(input('Choose 0 for Rock, 1 for Paper and 2 for Scissors!\n'))
comp = (random.randint(0,2))

if 0 <= choice_u <= 2:
    print(choice[choice_u])
print("Computer choose")
print(choice[comp])

if  3 <= choice_u < 0:
    print("Invalid choice!")
elif choice_u == 0 and comp == 2:
    print("You win")
elif choice_u == 2 and comp == 0:
    print("You lose")
elif choice_u > comp:
    print("You Win!")
elif comp > choice_u:
    print("You lose")
elif comp == choice_u:
    print("Its a draw")