import time

print("Thank you for choosing Python Pizza Deliveries! ")
size = input("What size pizza do you want? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇



def calculate_pizza_bill(size, add_pepperoni, extra_cheese):
    # Base prices
    if size == "S":
        bill = 15
        if add_pepperoni == "Y":
            bill += 2
    elif size == "M":
        bill = 20
        if add_pepperoni == "Y":
            bill += 3
    elif size == "L":
        bill = 25
        if add_pepperoni == "Y":
            bill += 3
    else:
        return "Invalid size"
    
    # Add extra cheese
    if extra_cheese == "Y":
        bill += 1
    
    return bill


final_bill = calculate_pizza_bill(size, add_pepperoni, extra_cheese)
print(f"Your final bill is: ${final_bill}")


#What DR ANGELA TYPED

