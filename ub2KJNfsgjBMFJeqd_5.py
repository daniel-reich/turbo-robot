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

from random import randrange
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = []
    #Initialize board
    for i in range(self.rows):
      self.board.append([])
      for j in range(self.cols):
        self.board[i].append(Cell(i,j))
    #Randomize Mines
    while(mines):
      mineRow, mineCol = randrange(0,rows), randrange(0,cols)
      if not self.board[mineRow][mineCol].mine:
        self.board[mineRow][mineCol].mine = True
        mines -= 1
    #Update neighbors
    for i in range(self.rows):
      for j in range(self.cols):
        if self.board[i][j].mine:
          for k in range(max(0,i-1),min(self.rows,i+2)):
            for l in range(max(0,j-1),min(self.cols,j+2)):
              if not (i==k and j==l):
                self.board[k][l].neighbors += 1
class Cell:
  def __init__(self,row,col):
    self.row = row
    self.col = col
    self.mine = False
    self.flag = False
    self.open = False
    self.neighbors = 0
  def __repr__(self):
    return '*' if self.mine else '_'

