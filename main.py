import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

# Design Connect Four
# Background
# Connect Four is a popular game played on a 7x6 grid. Two players take turns dropping colored discs into the grid.
# The first player to get four discs in a row (vertically, horizontally or diagonally) wins.



# Requirements
# Some possible questions to ask:
#
# What are the rules of the game?
# What size is the grid?
# How many players are there? Player vs Computer? Player vs Player?
# Are we keeping track of the score?
# Basics
# The game will be played by only two players, player vs player
# The game board should be of variable dimensions
# The target is to connect N discs in a row (vertically, horizontally or diagonally)
# N is a variable (e.g. connect 4, 5, 6, etc)
# There should be a score tracking system
# After a player reaches the target score, they are the winner
# Design
# High-level
# We will need a Grid class to maintain the state of the 2-D board
# The board cell can be empty, yellow (occupied by Player 1) or red (occupied by Player 2)
# The grid will also be responsible for checking for a win condition
# We can have a Player class to represent the player's piece color
# This isn't super important, but encapsulating information is generally a good practice
# The Game class will be composed of the Grid and Players
# The Game class will be responsible for the game loop and keeping track of the score

class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor

    def getName(self):
        return self._name

    def getPieceColor(self):
        return self._pieceColor


# The Grid will maintain the state of the board and all of the pieces. It will also check for a win condition.
# Perhaps it would be more appropriate to name the checkWin method to checkNConnected, since the Grid itself
# shouldn't need to know what the rules of the game are.

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()

    def initGrid(self):
        self._grid = [[GridPosition.EMPTY for _ in range(self._columns)] for _ in range(self._rows)]

    def getGrid(self):
        return self._grid

    def getColumnCount(self):
        return self._columns

    def placePiece(self, column, piece):
        if column < 0 or column >= self._columns:
            raise ValueError('Invalid column')
        if piece == GridPosition.EMPTY:
            raise ValueError('Invalid piece')
        for row in range(self._rows-1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row

    def checkWin(self, connectN, row, col, piece):
        count = 0
        # Check horizontal
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check vertical
        count = 0
        for r in range(self._rows):
            if self._grid[r][col] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check diagonal
        count = 0
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False

# The Game class will be used to play the game. It will keep track of the players, the score, and the grid.
# It will also be responsible for the game loop. The game parameters passed in via the constructor give us flexibility to
# play the game with slightly different rules and dimensions. While we could instantiate the board within the Game class,
# it's preferred to pass it in via the constructor. This means the Game class does not need to know how to instantiate the board.' \
#   ' Even though we are only playing with two players, we can still use a list to store the players. This is not necessary, but ' \
#   'it's easy enough and gives us flexibility to add more players in the future.

class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', GridPosition.YELLOW),
            Player('Player 2', GridPosition.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def printBoard(self):
        print('Board:\n')
        grid = self._grid.getGrid()
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += '0 '
                elif piece == GridPosition.YELLOW:
                    row += 'Y '
                elif piece == GridPosition.RED:
                    row += 'R '
            print(row)
        print('')

    def playMove(self, player):
        self.printBoard()
        print(f"{player.getName()}'s turn")
        colCnt = self._grid.getColumnCount()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add piece: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
        return (moveRow, moveColumn)

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round")
            maxScore = max(self._score[winner.getName()], maxScore)

            self._grid.initGrid() # reset grid
        print(f"{winner.getName()} won the game")



grid = Grid(6, 7)
game = Game(grid, 4, 2)
game.play()
