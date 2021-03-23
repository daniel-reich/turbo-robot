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

from random import sample
​
​
class Game:
​
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows, self.cols = rows, cols
    self.mines = mines
    self.gen_board()
  
  def gen_board(self):
    self.board = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
    for cell in sample([i for row in self.board for i in row], self.mines):
      cell.mine = True
    for cell in (i for row in self.board for i in row):
      cell.count_neighbors(self.board)
​
​
class Cell:
​
  def __init__(self, row, col):
    self.row, self.col = row, col
    self.mine = False
    self.flag = False
    self.open = False
    
  def count_neighbors(self, b):
    self.neighbors = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        nbr, nbc = self.row + i, self.col + j
        if (0 <= nbr < len(b)) and (0 <= nbc < len(b[0])):
          self.neighbors += b[nbr][nbc].mine
    self.neighbors -= self.mine

