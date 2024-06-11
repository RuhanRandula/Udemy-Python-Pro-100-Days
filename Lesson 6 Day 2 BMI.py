height = input("Enter your height in meters ")
weight = input("Enter your weight in KG ")

height= float(height)
weight= float(weight)



BMI = weight / height

print("Your BMI is ", int(BMI) )


#What was written by Dr.Angela
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)