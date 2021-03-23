"""


Create a function that takes a 5x5 3D list and returns `True` if it has at
least one Bingo, and `False` if it doesn't.

### Examples

    bingo_check([
      [45, "x", 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, 39, 44],
      [21, "x", 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      ["x", 43, 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, 65, "x", 83, 54],
      [67, 98, 39, "x", 44],
      [21, 59, 24, 30, "x"]
    ]) ➞ True
    
    bingo_check([
      ["x", "x", "x", "x", "x"],
      [64, 12, 47, 32, 90],
      [37, 16, 68, 83, 54],
      [67, 19, 98, 39, 44],
      [21, 75, 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      [45, "x", 31, 74, 87],
      [64, 78, 47, "x", 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, "x", 44],
      [21, "x", 24, 30, 52]
    ]) ➞ False

### Notes

Only check for diagnols, horizontals and verticals.

"""

def bingo_check(board):
​
  class Board:
​
    def __init__(self, board):
​
      self.board = board
      self.cols = []
​
      for n in range(len(self.board[0])):
        col = []
        for row in self.board:
          col.append(row[n])
        self.cols.append(col)
      
      d1 = []
      d2 = []
​
      num = 0
​
      for n in range(len(self.board)):
        d1.append(self.board[n][num])
        num += 1
        d2.append(self.board[n][-num])
      
      self.diags = [d1, d2]
​
      self.bingo = False
​
      for row in self.board:
        if list(set(row)) == ['x']:
          self.bingo = True
          break
      
      for col in self.cols:
        if list(set(col)) == ['x']:
          self.bingo = True
          break
      
      for diag in self.diags:
        if list(set(diag)) == ['x']:
          self.bingo = True
          break
      
  board = Board(board)
​
  return board.bingo

