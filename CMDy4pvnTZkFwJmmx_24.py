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
  def __init__(self,string):
    self.board = []
    for i in range(0,len(string),9):
      self.board.append([int(x) for x in string[i:i+9]])
  
  def get_row(self,row):
    return self.board[row]
  
  def get_col(self,col):
    columns = [[i[j] for i in self.board] for j in range(9)]
    return columns[col]
    
  def get_sqr(self,n,m=-1):
    if m<0:
      if n<3:
        rows = [0,1,2]
      elif 3<=n<6:
        rows = [3,4,5]
      else:
        rows = [6,7,8]
      if n%3==0:
        cols = [0,1,2]
      elif n%3==1:
        cols = [3,4,5]
      else:
        cols = [6,7,8]
      lst = []
      for r in rows:
        for c in cols:
          lst.append(self.board[r][c])
      return lst
    else:
      if n<3:
        return self.get_sqr(0) if m<3 else self.get_sqr(1) if 3<=m<6 else self.get_sqr(2)
      elif 3<=n<6:
        return self.get_sqr(3) if m<3 else self.get_sqr(4) if 3<=m<6 else self.get_sqr(5)
      else:
        return self.get_sqr(6) if m<3 else self.get_sqr(7) if 3<=m<6 else self.get_sqr(8)

