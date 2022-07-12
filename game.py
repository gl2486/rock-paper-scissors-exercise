

# this is the "game.py" file...

import os

player_name = os.getenv("PLAYER_NAME", default="Player One")

# def param

def divider_param(message):
    print('-' * 20)
    print(message)
    print('-' * 20)


divider_param(f"Welcome '{player_name}' to my Rock-Paper-Scissors game... \nROCK, PAPER, SCISSORS, SHOOT!")

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

divider_param(f"You chose: '{user_action.upper()}' \nThe computer chose: '{computer_action.upper()}'")


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


divider_param("Thanks for playing. Please play again!")
