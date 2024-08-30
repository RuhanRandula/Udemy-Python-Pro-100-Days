# Input a list of student scores
student_scores = input("Enter the list of student scores separated by spaces: ").split()
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row

# Initialize variables
total_score = 0
high_score = student_scores[0]  # Initialize high_score to the first score in the list

for score in student_scores:
    total_score += score
    if score > high_score:
        high_score = score

print(f"Total score is {total_score}")
print(f"Highest score is {high_score}")
