print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

while True:
    direction = input("Left or Right? ").lower()
    if direction == 'right':
        print("You fell in a hole. Game Over.")
        break
    elif direction == 'left':
        while True:
            swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
            if swim_wait == 'swim':
                print("You drowned under the powerful currents. Game Over.")
                exit()
            elif swim_wait == 'wait':
                while True:
                    which_door = input("You arrive at the island unharmed. There is a house with 3 doors, one red, one yellow and one blue. Which door do you choose? ").lower()
                    if which_door == 'red':
                        print("It's a room full of fire. Game Over.")
                        exit()
                    elif which_door == 'blue':
                        print("You enter a room filled with beasts. Game Over.")
                        exit()
                    elif which_door == 'yellow':
                        print("You found the treasure! You Win!")
                        exit()
                    else:
                        print("Please choose Red, Blue, or Yellow.")
            else:
                print("Please choose Swim or Wait.")
    else:
        print("Please choose Left or Right.") 