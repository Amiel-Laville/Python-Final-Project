# Chess Game - Introduction to Problem Solving and Programming in Python

This is my final project for my Introduction to Problem Solving and Programming in Python class. It's basically a chess game I made using Python.

## Files

**main.py**: This is where the game starts.

**chess_board.py**: Handles how the board works and keeps track of everything.

**pieces.py**: Defines all the chess pieces and how they move.

**player.py**: Controls the player and the AI.

## Installation

To run this, just make sure you have Python installed. Then clone the repo and run main.py to start playing.


## How to Play

When you run the game, you’ll first choose a game mode:

1 = Human vs AI
2 = Human vs Human
3 = AI vs AI

After that, the game will start and the board will be printed in the console.

Board Layout
The board is an 8x8 grid.
White pieces are at the bottom of the board.
Black pieces are at the top of the board.
Piece Symbols

Each piece is shown using a letter:

P / p = Pawn
R / r = Rook
N / n = Knight
B / b = Bishop
Q / q = Queen
K / k = King
Uppercase letters = White pieces
Lowercase letters = Black pieces
How to Enter Moves

When it’s your turn, you enter a move like this:

from_row from_col to_row to_col

This means:

The position your piece is moving from
The position you want to move it to
Example Moves
Move a white pawn forward:
6 0 5 0
Move a knight:
7 1 5 2
Move a rook:
7 0 5 0
Important Notes
Rows and columns are numbered from 0 to 7.
Row 0 is the top of the board (black side).
Row 7 is the bottom of the board (white side).
If you enter an invalid move, the game will ask you to try again.
