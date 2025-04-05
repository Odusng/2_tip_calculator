print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_perc = tip / 100
total_tip = bill * tip_perc
total_bill = bill + total_tip
ind_bill = total_bill / people
final_bill = round(ind_bill, 2)
print(f"Each person should pay: {final_bill}")
