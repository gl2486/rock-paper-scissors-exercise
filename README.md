# Rock-Paper-Scissors

A command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer opponent.

# Setup

Optionally clone or download this [remote repository](https://github.com/gl2486/rock-paper-scissors-exercise) onto your local computer,  for example *Desktop*. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/game.py
```

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

# Usage
## Game Play

Play a game:

```sh
python game.py
```

Option to play the game with PLAYER_NAME (e.g. 'Jon Snow') selection:

```sh
PLAYER_NAME="Jon Snow" python game.py
```
## Rules of the Game

The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper
- Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

# Demo

Here is a demonstration of the game play:

```
--------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
ROCK, PAPER, SCISSORS, SHOOT!
--------------------
Please choose either 'ROCK', 'PAPER' or 'SCISSORS': rock
--------------------
You chose: 'ROCK'
The computer chose: 'PAPER'
--------------------
Oh, the computer won. Better luck next time!
--------------------
Thanks for playing. Please play again!
--------------------
```