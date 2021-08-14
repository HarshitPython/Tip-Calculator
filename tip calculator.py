print("Welcome to the tip calculator")

# Total bill
bill = float(input("What was the total bill ? $"))

# Tip % you want to give
tip = int(input("What percentage would you like to give ? "))

people = int(input("How many people to split the bill ? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person,2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay : $ {final_amount}")
