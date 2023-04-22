#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
pretip_total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10,12 or 15? ")
people = input("How many people to split the bill? ")

pretip_total = float(pretip_total)
tip = int(tip)
people = int(people)

tip = (tip/100) * pretip_total

with_tip_total = pretip_total + tip
split_pay = round(with_tip_total/people, 2) 

print(f"Each person should pay: ${split_pay:.2f} ")
