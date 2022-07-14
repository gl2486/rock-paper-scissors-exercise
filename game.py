

# this is the "game.py" file...

import random
import os

def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    
    winners = {
        "rock":{
            "rock" :  None,
            "paper" : "paper",
            "scissors" : "rock",
        },
        "paper":{
            "rock" : "paper",
            "paper" : None,
            "scissors" : "scissors",
        },
        "scissors":{
            "rock" : "rock",
            "paper" : "scissors",
            "scissors" : None,
        },
    }
    
    # todo: write some Python here to determine the winner
    winner = winners[choice_1][choice_2]

    return winner



# def param

def divider_param(message):
    print('-' * 20)
    print(message)
    print('-' * 20)



if __name__ == "__main__":


    # Customize player name

    player_name = os.getenv("PLAYER_NAME", default="Player One")




    divider_param(f"Welcome '{player_name}' to my Rock-Paper-Scissors game... \nROCK, PAPER, SCISSORS, SHOOT!")


    # user action input
    # list possible actions
    # validate input, casefold
    # added loop

    while True:

        user_action = input("Please choose either 'ROCK', 'PAPER' or 'SCISSORS': ").lower()
        possible_actions = ["rock", "paper", "scissors"]

        if user_action not in possible_actions:
            print("Oops, please try again!")
            continue

        else:
            break


    # computer random selection..

    computer_action = random.choice(possible_actions)


    # print user input and computer selection

    divider_param(f"You chose: '{user_action.upper()}' \nThe computer chose: '{computer_action.upper()}'")

    # DETERMINE WINNER
    # Rock beats Scissors
    # Paper beats Rock
    # Scissors beats Paper
    # Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

    #win = {
    #    'paper':'scissors', 
    #    'rock':'paper', 
    #    'scissors':'rock'
    #}
#
    #if user_action == win[computer_action]:
    #    print("Congrats! you win.")
    #elif computer_action == win[user_action]:
    #    print("Oh, the computer won. Better luck next time!")
    #else:
    #    print("It's a tie!")

    winning_action = determine_winner(user_action,computer_action)
    #print(winning_action)
    if winning_action == user_action:
        print("Congrats! you won.")
    elif winning_action == computer_action:
        print("Oh, the computer won. Better luck next time!")
    else:
        print("It's a tie!")


    divider_param("Thanks for playing. Please play again!")
