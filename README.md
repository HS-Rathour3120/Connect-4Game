# Connect-4Game
Connect Four is a popular game played on a 7x6 grid. Two players take turns dropping colored discs into the grid. The first player to get four discs in a row (vertically, horizontally or diagonally) wins.

Requirements
Some possible questions to ask:

What are the rules of the game?
What size is the grid?
How many players are there? Player vs Computer? Player vs Player?
Are we keeping track of the score?
Basics
The game will be played by only two players, player vs player
The game board should be of variable dimensions
The target is to connect N discs in a row (vertically, horizontally or diagonally)
N is a variable (e.g. connect 4, 5, 6, etc)
There should be a score tracking system
After a player reaches the target score, they are the winner
Design
High-level
We will need a Grid class to maintain the state of the 2-D board
The board cell can be empty, yellow (occupied by Player 1) or red (occupied by Player 2)
The grid will also be responsible for checking for a win condition
We can have a Player class to represent the player's piece color
This isn't super important, but encapsulating information is generally a good practice
The Game class will be composed of the Grid and Players
The Game class will be responsible for the game loop and keeping track of the score
