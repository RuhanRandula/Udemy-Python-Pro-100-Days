# # Function to add the digits of a two-digit number
# def add_digits(number):
#     # Ensure the number is a two-digit number
#     if 10 <= number <= 99:
#         # Extract the tens and units digits
#         tens = number // 10
#         units = number % 10
#         # Calculate the sum of the digits
#         sum_of_digits = tens + units
#         return f"{tens} + {units} = {sum_of_digits}"
#     else:
#         return "Please enter a valid two-digit number."

# # Main code
# # Get user input
# number = int(input("Enter a two-digit number: "))

# # Call the function and print the result
# print(add_digits(number))

two_digit_number = input("Enter a two-digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(f"{first_digit} + {second_digit}")