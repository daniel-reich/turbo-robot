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
  def __init__(self, rows=14, cols=18, mines=40):
    Cell.count = 0
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = [[Cell(r, c, mines) for c in range(cols)] for r in range(rows)]
    
    for row in self.board:
      for cell in row:
        around = []
        x = cell.row
        y = cell.col
        coords = [[x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], 
                  [x, y+1], [x+1,y-1], [x+1,y], [x+1,y+1]]
        for coord in coords:
          if coord[0] >= 0 and coord[1] >= 0:
            try:
              around.append(self.board[coord[0]][coord[1]].mine)
            except IndexError:
              pass
        cell.bombs_around(sum(around))
​
class Cell:
  count = 0
  def __init__(self, row, col, mines):
    self.row = row
    self.col = col
    
    self.mine = False
    if Cell.count < mines:
      self.mine = True
    Cell.count += 1
    
    self.flag = False
    self.open = False
    self.neighbors = None
    
  def bombs_around(self, the_sum):
    self.neighbors = the_sum

