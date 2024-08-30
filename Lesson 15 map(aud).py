line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Enter position (e.g., b2): ")  # Prompting user for input

# Extract the row and column from the input
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)  # Convert letter to column index

number_index = int(position[1]) - 1  # Convert number to row index

# Place the "X" on the map based on user input
map[number_index][letter_index] = "X"

# Print the updated map
print(f"{line1}\n{line2}\n{line3}")
