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
  def nearby(space, max_row, max_col):
    space = [int(i) for i in space.split(',')]
    
    row = space[0]
    col = space[1]
​
    if row == 0:
      nearby_rows = [row + 1, row]
    elif row == max_row:
      nearby_rows = [row - 1, row]
    else:
      nearby_rows = [row - 1, row, row + 1]
    
    if col == 0:
      nearby_cols = [col + 1, col]
    elif col == max_col:
      nearby_cols = [col - 1, col]
    else:
      nearby_cols = [col - 1, col, col + 1]
    
    nearby = []
​
    for row in nearby_rows:
      for col in nearby_cols:
        spae = '{},{}'.format(row, col)
        if spae != ','.join([str(s) for s in space]):
          nearby.append(spae)
    
    return nearby
  def __init__(self, num_of_rows = 14, num_of_cols = 18, num_of_mines = 40):
    from random import randint as r
    self.rows = num_of_rows
    self.cols = num_of_cols
    self.mines = num_of_mines
​
    mined_counts = []
​
    for n in range(self.mines):
      rand = r(0, (self.rows * self.cols)-1)
      while rand in mined_counts:
        rand = r(0, (self.rows * self.cols)-1)
      mined_counts.append(rand)
    
    to_mine_spaces = {}
    count = 0
​
    for row in range(self.rows):
      for col in range(self.cols):
        mined = False
        if count in mined_counts:
          mined = True
        to_mine_spaces['{},{}'.format(row, col)] = mined
        count += 1
    
    nearby_spaces = {}
​
    for space in to_mine_spaces.keys():
      nearby = Game.nearby(space, self.rows-1, self.cols-1)
      nearby_spaces[space] = nearby
    
    mines_nearby = {}
​
    for space in to_mine_spaces.keys():
      count = 0
      for s in nearby_spaces[space]:
        if to_mine_spaces[s] == True:
          count += 1
      mines_nearby[space] = count
    
    self.board = []
​
    for row in range(self.rows):
      r = []
      for col in range(self.cols):
        space = '{},{}'.format(row, col)
        cell = Cell(row, col, to_mine_spaces[space], mines_nearby[space])
        r.append(cell)
      self.board.append(r)
​
​
  
​
class Cell:
​
  def __init__(self, row, col, mine, mined_neighbors, flag = False, opn = False):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = flag
    self.open = opn
    self.neighbors = mined_neighbors

