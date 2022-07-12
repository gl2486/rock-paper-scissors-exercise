# Rock-Paper-Scissors

A command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer opponent.

# Setup

Optionally clone or download this [remote repository](https://github.com/gl2486/rock-paper-scissors-exercise) onto your local computer,  for example *Desktop*. Then navigate to wherever you downloaded the repo:

```
cd ~/Desktop/game.py
```

Create a virtual environment:

```
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```
conda activate rps-env
```

Install package dependencies within the virtual environment:

```
pip install -r requirements.txt
```



# Usage
## Game Play

Play a game

```
python game.py
```

Select a PLAYER_NAME (e.g. 'Jon Snow') to play the game

```
PLAYER_NAME="Jon Snow" python game.py
```


# Demo

Here is a demonstration of the gameplay:

```
--------------------
ROCK, PAPER, SCISSORS, SHOOT!
--------------------
Please choose either 'ROCK', 'PAPER' or 'SCISSORS': scissors
--------------------
You chose: 'SCISSORS'
The computer chose: 'ROCK'
--------------------
Oh, the computer won. Better luck next time!
--------------------
Thanks for playing. Please play again!
```