


# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = weight / (height ** 2)

if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 25:
    print("You are at a normal weight")
elif 25 <= BMI < 30:
    print("You are slightly overweight")
elif 30 <= BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")

# WHAT DR ANGELA TYPED

height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")