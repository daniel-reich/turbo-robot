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

class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.__minecount__ = 0
    self.board = [[
      Cell(row, col, self.__lay_mine__(), self) for col in range(0, cols)
    ] for row in range(0, rows)]
​
  def __lay_mine__(self):
    if self.__minecount__ >= self.mines:
      return False
    self.__minecount__ += 1
    return True
    
  def __str__(self):
    return '\n'.join(['|'.join([str(cell) for cell in row]) for row in self.board])
      
​
class Cell:
  def __init__(self, row, col, mine, game):
    self.row = row
    self.col = col
    self.mine = mine
    self.game = game
    self.flag = False
    self.open = False
    
  @property
  def neighbors(self):
    top_index = max(self.row - 1, 0)
    bottom_index = min(self.row + 2, self.game.rows)
    left_index = max(self.col - 1, 0)
    rightIndex = min(self.col + 2, self.game.cols)
    mines = []
    for row in self.game.board[top_index:bottom_index]:
      mines += [1 if cell.mine else 0 for cell in row[left_index:rightIndex]]
    return sum(mines) - (1 if self.mine else 0)
      
  def __str__(self):
    return 'X' if self.mine else ' '

