#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
tbill_int = float(total_bill)

per_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
ptip_int = int(per_tip)

total_people = input("How many people to split the bill? ")
tpeople_int = int(total_people)

res = (tbill_int / tpeople_int) * (ptip_int / 100 + 1)
res = round(res, 2)

print(f"Each person should pay: ${res}")