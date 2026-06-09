print("Welcome to Tip Calculator")
original_bill = float(input("\nWhat was your total bill\n₹"))
tip = int(input("How much tip would you like to give as percent\n: "))
person = int(input("How many people to split the bill\n: "))

tip_as_percent = tip / 100
final_bill = original_bill + (original_bill * tip_as_percent)
per_person_bill = final_bill / person

print(f"\nEach person should pay ₹{per_person_bill:.2f}")
