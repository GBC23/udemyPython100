import random

user_choice = input('0 for Rock, 1 for Paper, 2 for Scissors : ')

user_choice_int = int(user_choice)

computer_choice = random.randint(0,2)

# computer_choice(0) == 'Rock'
# computer_choice(1) == 'Paper'
# computer_choice(2) == 'Scissors'

if computer_choice == 0:
    print("Computer's choice = Rock")
elif computer_choice == 1:
    print('Computer\'s choice = Paper')
else:
    print('computer\'s choice = Scissors')

# print(type(user_choice_int1))
if user_choice_int == computer_choice:
    print('Draw.')
elif user_choice_int == 0 and computer_choice == 1:
    print('You lose')
elif user_choice_int == 0 and computer_choice == 2:
    print('You win!')
elif user_choice_int == 1 and computer_choice == 0:
    print('You win!')
elif user_choice_int == 1 and computer_choice == 2:
    print('You lose')
elif user_choice_int == 2 and computer_choice == 0:
    print('You lose')
elif user_choice_int == 2 and computer_choice == 1:
    print('You win!')
else:
    print('Error occured. You lose')