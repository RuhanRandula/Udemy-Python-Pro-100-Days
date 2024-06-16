# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# age_as_int = int(age)

# life_expectancy_as_int = 90
# weeks_in_a_year_as_int = 52

# weeks_left_as_int = (life_expectancy_as_int-age_as_int) * weeks_in_a_year_as_int

# print("You have" + {weeks_left_as_int} + "remaining")


#What Dr Angela Wrote
age = input("What is your age? ")
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
