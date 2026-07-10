print("Welcome to Python pizza")
size = input("What size of pizza do you want S, M or L? ")
pepperoni = input("Do you want pepperoni (Y/N)? ")
extra_cheese = input("Do you want extra cheese? (Y/N)")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry, please enter S, M, or L.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"You have to pay ${bill}")