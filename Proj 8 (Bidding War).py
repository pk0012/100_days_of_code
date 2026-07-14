from art_bid import logo
print(logo)

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

name_bids = {}
bid_cont = True
while bid_cont:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid:$ "))
    for bids in name:
        name_bids[name] = bid

    cont = input("Are there any other bidders? (y/n): ")
    if cont == "n":
        bid_cont = False
        highest_bidder(name_bids)
    elif cont == "y":
        bid_cont = True
        print("\n" * 30)
