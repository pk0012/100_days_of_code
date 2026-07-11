print("Welcome to Roller Coaster")

height = int(input("What is your Height? "))
bill = 0


if height >= 120:
    print("You are allowed to ride the Roller Coaster.")
    age = int(input("What is your Age? "))
    if age <= 12:
        bill = 5
        print("You have to pay $5.")
    elif age <= 18:
        bill = 7
        print("You have to pay $7.")
    elif 45 <= age <= 55:
        bill = 0
        print("Ah! You're having a Midlife Crisis. The ride's on us.")
    else :
        bill = 12
        print("You have to pay $12.")
    wants_photo = input("Do you wish to have a photo for $3 extra? (y/n)")
    if wants_photo == "y":
        bill += 3
    print(f"You have to pay ${bill}.")

else:
    print("You are not allowed to ride the Roller Coaster.")

