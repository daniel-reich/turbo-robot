"""


In this challenge we're going to build a board for a **Minesweeper** game
using **OOP**. Create two classes: `Game` and `Cell`.

`Game` should take in 3 arguments: number of **rows** , number of **columns**
and total number of **mines** , set the default values to 14, 18 and 40
respectively. Each instance should have attributes `.rows`, `.cols` and
`.mines`, equivalent to the values of the three arguments. It should also have
a `.board` attribute, the board shoud be a 2-D list with _rows_ sublists with
_cols_ instances of `Cell`.

A `Cell` should have attributes `.row` and `.col`, set these to its position
on the board. Attributes `.mine` (either `True` or `False`), `.flag` and
`.open` (set both to `False`). Finally an attribute `.neighbors`, indicating
how many of its neighboring cells are mined.

### Tests

    game = Game()
    game.rows ➞ 14
    game.cols ➞ 18
    game.mines ➞ 40
    height of .board ➞ 14
    width of .board ➞ 18
    Cells in .board ➞ 252
    total mined in cells .board ➞ 40
    each Cell .row and .col attributes match its position on the board ➞ True
    each Cell .flag and .open attributes are set to False ➞ True
    each Cell .neighbors attribute matches the actual amount of neighboring mines ➞ True

### Notes

  * Try randomizing the position of the mines.
  * Feel free to add as many other attributes or methods as you need.

"""

import random
class Game(object):
  def __init__(self, rows = 14, cols = 18, mines = 40):
      self.rows = rows
      self.cols = cols
      self.mines = mines
      #self.board = [[Cell(i, j) for j in range(columns)] for i in range(rows)]
      self.board = [[ "" for j in range(cols)] for i in range(rows)]
      countermines = 0
      for i in range(rows):
          for j in range(cols):
              tmpcell = Cell(i, j)
              if tmpcell.mine:
                  countermines += 1
                  if countermines > self.mines:
                      tmpcell.mine = False
              self.board[i][j] = tmpcell
      for row in self.board:
          for cell in row:
              cell.checkneighbors(self.rows, self.cols, self.board)
​
class Cell(object):
    def __init__(self, row=0, col= 0):
        self.row = row
        self.col = col
        self.mine = True
        self.flag = False
        self.open = False
        self.neighbors = 0
        
    def checkneighbors(self, rows, columns, board):
        neighbors = [[self.row -1, self.col -1],[self.row -1, self.col],[self.row -1, self.col +1],[self.row, self.col -1],[self.row, self.col +1], [self.row +1, self.col -1],[self.row +1, self.col],[self.row +1, self.col +1],]
        nearmines = 0
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < rows and neighbor[1] >= 0 and neighbor[1] < columns:
                if board[neighbor[0]][neighbor[1]].mine:
                    nearmines += 1
        self.neighbors = nearmines

