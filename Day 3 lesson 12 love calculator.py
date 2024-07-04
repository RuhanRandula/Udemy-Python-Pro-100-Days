print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?


# Function to calculate the love score
def love_score(name1, name2):


    combined_names = name1 + name2
    combined_names_lower = combined_names.lower()

    # Count occurrences of the letters in "TRUE"
    t = combined_names_lower.count('t')
    r = combined_names_lower.count('r')
    u = combined_names_lower.count('u')
    e = combined_names_lower.count('e')
    true_score = t + r + u + e

    # Count occurrences of the letters in "LOVE"
    l = combined_names_lower.count('l')
    o = combined_names_lower.count('o')
    v = combined_names_lower.count('v')
    e = combined_names_lower.count('e')
    love_score = l + o + v + e

    # Combine the scores to form a 2-digit number
    final_score = int(str(true_score) + str(love_score))

    # Determine the message based on the final score
    if final_score < 10 or final_score > 90:
        print(f"Your score is {final_score}, you go together like coke and mentos.")
    elif 40 <= final_score <= 50:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}.")
        
love_score(name1, name2)

