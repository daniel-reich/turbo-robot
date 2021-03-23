"""


Create a class `Sudoku` that takes a **string** as an argument. The string
will contain the numbers of a regular 9x9 sudoku board **left to right and top
to bottom** , with zeros filling up the empty cells.

### Attributes

An instance of the class `Sudoku` will have one attribute:

  * `board`: a list representing the board, with sublits for each **row** , with the numbers as **integers**. Empty cell represented with `0`.

### Methods

An instance of the class `Sudoku` wil have three methods:

  * `get_row(n)`: will return the row in position `n`.
  * `get_col(n)`: will return the column in position `n`.
  * `get_sqr([n, m])`: will return the square in position `n` if only one argument is given, and the square to which the cell in position `(n, m)` belongs to if two arguments are given.

### Example

![Sudoku picture](https://edabit-
challenges.s3.amazonaws.com/sudoku_hard_039.gif)

    game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
    
    game.board ➞ [
      [4, 1, 7, 9, 5, 0, 0, 3, 0],
      [0, 0, 0, 0, 0, 0, 7, 0, 0],
      [0, 6, 0, 0, 0, 7, 0, 0, 0],
      [0, 5, 0, 0, 0, 9, 1, 0, 6],
      [8, 0, 0, 6, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 4, 0, 0],
      [9, 0, 0, 0, 0, 5, 0, 0, 0],
      [0, 0, 0, 4, 3, 0, 0, 0, 0],
      [2, 0, 0, 7, 0, 1, 5, 8, 0]
    ]
    
    game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
    game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
    game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
    game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
    game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

### Notes

  * All positions are indexed to 0.
  * All orders are assigned left to right and top to bottom.

"""

class Sudoku:
  def __init__(self, board):
    self.board = [[int(board[r*9+c]) for c in range(9)] for r in range(9)]
  def get_row(self, n):
    return self.board[n]
  def get_col(self, n):
    return [row[n] for row in self.board]
  def get_sqr(self, n, m=None):
    if m == None:
      r, c = (n//3)*3, (n%3)*3
    else:
      r, c = (n//3)*3, (m//3)*3
    return [self.board[r][c], self.board[r][c+1], self.board[r][c+2],
            self.board[r+1][c], self.board[r+1][c+1], self.board[r+1][c+2],
            self.board[r+2][c], self.board[r+2][c+1], self.board[r+2][c+2]]

