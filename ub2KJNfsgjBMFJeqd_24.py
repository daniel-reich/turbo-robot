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
​
def get_random_board_pos(board):
  return board[random.choice(range(len(board)))][random.choice(range(len(board[0])))]
​
​
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    #mine_coords = [(random.choice(range(self.cols)), random.choice(range(self.rows))) for m in range(self.mines)]
    self.board = [[Cell(row=r,col=c)  for c in range(self.cols)] for r in range(self.rows)]
    for m in range(mines):
      cell = get_random_board_pos(self.board)
      while cell.mine:
        cell = get_random_board_pos(self.board)
      cell.set_mine(self)
      
  def get_cell(self, row, col):
    return self.board[row][col]
      
​
class Cell:
  def __init__(self, row, col, flag=False, o=False, mine=False):
    self.row = row
    self.col = col
    self.flag= flag
    self.open = o
    self.neighbors = 0
    self.mine = mine
    
  def get_neighbors(self):
    col = self.col
    row = self.row
    return [(row - 1,col - 1), (row, col - 1), (row + 1, col - 1), (row - 1, col), (row + 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
    
  def set_mine(self, game):
    self.mine = True
    for r,c in self.get_neighbors():
      if r >= 0 and c >= 0 and r < game.rows and c < game.cols:
        game.get_cell(r,c).neighbors += 1

