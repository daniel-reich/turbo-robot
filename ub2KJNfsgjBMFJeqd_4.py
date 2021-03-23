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
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = []
    self.init_board()
  def i_bomb(self, cl):
    surrounding = [
    (cl.col + 1, cl.row), (cl.col + 1, cl.row + 1), (cl.col, cl.row + 1), (cl.col - 1, cl.row + 1), 
    (cl.col - 1, cl.row), (cl.col - 1, cl.row - 1), (cl.col, cl.row - 1), (cl.col + 1, cl.row - 1),
    ]
    num_s = 0
    for coord in surrounding:
      if coord[0] < 0 or coord[0] >= self.cols or coord[1] < 0 or coord[1] >= self.rows:
        continue
      if self.board[coord[1]][coord[0]].mine:
        num_s += 1
    cl.neighbors = num_s
​
  def bomb_updater(self):
    for row in self.board:
      for c in row:
        self.i_bomb(c)
​
​
  def init_board(self):
    #generating bombs coords
    p_m_coord_ls = []
    if self.mines > self.rows * self.cols:
      raise ValueError('Number of mines exceed number of available cells.')
    i = 0
    while i < self.mines:
      y0 = random.randint(0, self.rows - 1)
      x0 = random.randint(0, self.cols - 1)
      if (x0, y0) in p_m_coord_ls:
        continue
      p_m_coord_ls.append((x0, y0))
      i += 1
    #placing everything by row
    for y in range(self.rows):
      row = []
      for x in range(self.cols):
        if (x, y) in p_m_coord_ls:
          row.append(Cell(y, x, True))
        else:
          row.append(Cell(y, x, False))
      self.board.append(row[:])
    #updating b
    self.bomb_updater()
​
​
class Cell:
  def __init__(self, row, col, mine):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = 0

