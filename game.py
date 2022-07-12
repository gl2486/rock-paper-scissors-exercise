

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


# DETERMINE WINNER
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

win = {
    'paper':'scissors', 
    'rock':'paper', 
    'scissors':'rock'
}

if user_action == win[computer_action]:
    print("Great job, you win!")
elif computer_action == win[user_action]:
    print("Oh, the computer won. Better luck next time!")
else:
    print("It's a tie!")

print('-' * 20)
print("Thanks for playing. Please play again!\n")
