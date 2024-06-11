# print("Welcome to the tip calculator! ")

# bill = float(input("What was the total bill? "))

# tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# people = float(input("How many people to split the bill? "))

# tip_as_percent = tip/100

# per_person = (bill/people) * tip_as_percent

# print(f"Each person should pay: ${round(per_person)}")

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the tip as a percentage of the total bill
tip_as_percent = tip / 100

# Calculate the total bill including tip
total_bill_with_tip = bill * (1 + tip_as_percent)

# Calculate the amount each person should pay
per_person = total_bill_with_tip / people

print(f"Each person should pay: ${round(per_person, 2)}")
