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

from random import shuffle
import numpy as np
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.create_minefield()
    self.create_neighborsfield()
    self.create_board()   
  
  def create_minefield(self):
    self.minefield = [True for x in range(self.mines)] + [False for x in range((self.rows*self.cols)-self.mines)]
    shuffle(self.minefield)
    self.minefield = np.array(self.minefield).reshape(self.rows,self.cols)
​
  def create_neighborsfield(self):
    self.neighborsfield = np.zeros((self.rows,self.cols))
    for c in range(self.cols):
      for r in range(self.rows):      
        n = 1
        r1 = max(r-n,0)
        r2 = min(r+n+1, self.rows)
        c1 = max(c-1,0)
        c2 = min(c+n+1, self.cols)
        self.neighborsfield[r,c] = self.minefield[r1:r2,c1:c2].sum()
​
        if self.minefield[r,c] == 1:
          self.neighborsfield[r,c] -= 1
​
  def create_board(self):
    self.board = [[Cell(r,c,self.minefield[r,c],self.neighborsfield[r,c]) for c in range(self.cols)] for r in range(self.rows)]
​
class Cell:
  def __init__(self, row, col, mine, neighbors):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors

