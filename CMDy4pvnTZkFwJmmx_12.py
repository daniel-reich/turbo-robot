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
    blst = []
    for i in board:
      blst.append(int(i))
    self.boardlst = blst
    self.board = [self.boardlst[0:9],self.boardlst[9:18], self.boardlst[18:27],self.boardlst[27:36],
    self.boardlst[36:45], self.boardlst[45:54], self.boardlst[54:63], self.boardlst[63:72], self.boardlst[72:81]]
    self.squares = {0:self.board[0][0:3]+self.board[1][0:3]+self.board[2][0:3]}
    self.squares[1] = self.board[0][3:6]+self.board[1][3:6]+self.board[2][3:6]
    self.squares[2] = self.board[0][6:9]+self.board[1][6:9]+self.board[2][6:9]
    self.squares[3] = self.board[3][0:3]+self.board[4][0:3]+self.board[5][0:3]
    self.squares[4] = self.board[3][3:6]+self.board[4][3:6]+self.board[5][3:6]
    self.squares[5] = self.board[3][6:9]+self.board[4][6:9]+self.board[5][6:9]
    self.squares[6] = self.board[6][0:3]+self.board[7][0:3]+self.board[8][0:3]
    self.squares[7] = self.board[6][3:6]+self.board[7][3:6]+self.board[8][3:6]
    self.squares[8] = self.board[6][6:9]+self.board[7][6:9]+self.board[8][6:9]    
    
  def get_row(self, row):
    return self.board[row]
    
  def get_col(self, col):
    c = []
    for i in range(0, len(self.board)):
      c.append(self.board[i][col])
    return c
    
  def get_sqr(self, *n):
    try:
      if n[1] < 3:
        if n[0] <3: return self.squares.get(0)
        elif n[0] < 6: return self.squares.get(3)
        else: return self.squares.get(6)
      elif n[1] < 6:
        if n[0] <3: return self.squares.get(1)
        elif n[0] < 6: return self.squares.get(4)
        else: return self.squares.get(7)
      else:
        if n[0] < 3: return self.squares.get(2)
        elif n[0] < 6: return self.squares.get(5)
        else: return self.squares.get(8)
    except:
      return self.squares.get(n[0])

