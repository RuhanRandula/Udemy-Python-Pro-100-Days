# Input a Python list of student heights
student_heights = input("Enter a list of student heights separated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# Initialize total height and count of students
total_height = 0
number_of_students = 0

# Calculate total height and number of students
for height in student_heights:
    total_height += height  # Add each student's height to total
    number_of_students += 1  # Count each student

# Calculate average height
average_height = total_height / number_of_students

# Print the results
print(f"Total height = {total_height}")
print(f"Number of students = {number_of_students}")
print(f"Average height = {round(average_height)}")

