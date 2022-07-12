

# this is the "game.py" file...

print('-' * 20)
print("ROCK, PAPER, SCISSORS, SHOOT!")
print('-' * 20)


# user action input
# list possible actions
# "while" loops

while True:

    user_action = input("Please choose either 'ROCK', 'PAPER' or 'SCISSORS': ")
    possible_actions = ["rock", "paper", "scissors"]

    if user_action.casefold() not in possible_actions:
        print("Oops, please try again!")
        continue

    else:
        break


# import random
# computer random selection..

import random
computer_action = random.choice(possible_actions)


# print user input and computer selection

print('-' * 20)
print(f"You chose: '{user_action.upper()}' \nThe computer chose: '{computer_action.upper()}'")
print('-' * 20)
