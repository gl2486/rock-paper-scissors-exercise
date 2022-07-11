

# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")


# user action input 

user_action = input("Please choose either 'rock', 'paper' or 'scissors': ")


# list of possible actions
# computer random selection..

import random

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose: {user_action} \nComputer chose: {computer_action}\n")

