# Day 2: Tip Calculator
print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? "))
tip = int(input("What percent would you like to tip? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = total_tip + bill
final_bill = total_bill / split
tot_with_tip = round(final_bill, 2)

print(f"Each person should pay:${tot_with_tip}")