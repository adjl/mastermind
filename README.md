# Mastermind

## About
Python implementation of the classic board game 'Mastermind'

## Features
The game has three gameplay modes:
- Single-player, where a human plays against the computer
- Multiplayer, where humans play against each other
- Duel, where computer players play against each other

The game has an options screen where the user can change game settings:
- number of games, which must be even
- number of pegs, which must be 3-8
- number of colours, which must be 3-8

The game allows saving and loading to and from multiple game files. It also
checks for possible overwriting and prompts the user for confirmation. Humans
can only save during their turn as the codebreaker. That is, they cannot save
when the computer is solving.

On starting, the game asks for names to uniquely identify each player. Computer
players choose one from a list of available names.

At each turn, the game shows:
- the current game and turn number
- the total number of games and turns
- who the codemaker and codebreaker are
- the codemaker and codebreaker scores
- the number of pegs and the colours used in the current game set

To keep track of the running game, an ASCII board is displayed and continually
updated with each new guess and feedback. At the start of a new game, the board
is cleared.

## Technical Info
The game has a global signal handler which catches all KeyboardInterrupts
(Ctrl-C) and exits the game gracefully.

The solving algorithm works by first determing what colours are in the secret
pattern. After establishing the colours, an initial guess is made with those
colours. A list of possible solutions is then generated based on the initial
feedback. Then another guess is made using one of the possible solutions. A
new list of solutions is generated, but only those common to both the previous
and new lists are taken as real solutions (and hence reducing the solutions
space). Essentially, the algorithm guesses, generates then refines.

The solving algorithm runs slowly for feedback containing six or more white
pegs, so this only applies to games played with 6-8 pegs. Generally, the
greater the number of pegs, colours and white pegs, the slower the algorithm.

PyGTK is used to make the graphical user interface of the game.

## Usage
To start the text version of the game, run
```
$ ./mastermind.py -t # or simply
$ ./mastermind.py
```

To start playing, choose one of the three available modes [S, M, D]. You can
also change settings in the Options screen [O].

You will then be asked to enter your name and, when playing as the codemaker,
your secret pattern.

To enter a secret pattern or guess, just type in the first character of each
colour (e.g. 'rgby' for 'red green blue yellow').

When playing as the codebreaker, you can save by pressing Ctrl-D. Enter the
save file name when prompted. If the save file already exists, you will be
asked if you want to overwrite.

To load a game, choose Load [L] at the menu screen.

To start the graphical version of the game, run
```
$ ./mastermind.py -g
```

The method of entering a secret pattern or guess is similar to that in the text
version.

## Disclaimer
The ComputerPlayer names are taken from the games 'Portal' and 'Portal 2'. They
do not belong to me; they belong to Valve.

## Notes
Only multiplayer mode is enabled in the graphical version of the game. Saving
and loading are disabled.

## TODO
- Speed up solving algorithm
- Decouple game logic and interface code
- Implement single-player and duel modes in the graphical version
- Implement saving and loading in the graphical version

## License
[MIT License](LICENSE)
