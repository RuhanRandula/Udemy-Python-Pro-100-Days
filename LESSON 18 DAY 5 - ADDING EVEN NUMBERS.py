target = int(input("please enter a number between 1 and 1000: "))

total = 0

#Add all even numbers from 2 to target
for num in range(2, target+1, 2):
    total += num
    
    

print(total)
    
# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

