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

from random import randint
​
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = self.build_board(rows, cols, mines)
​
  def build_board(self, n, m, b):
    #build board
    board = [[Cell(x, y) for y in range(m)] for x in range(n)]
​
    #lay mines
    c = 0
    while c < b:
      i = randint(0,n-1)
      j = randint(0,m-1)
      if board[i][j].mine:
        pass
      else:
        board[i][j].mine = True
        c += 1
​
    #populate neighbors
    for i, row in enumerate(board):
      for j, cell in enumerate(row):
        adj = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        for x, y in adj:
          if i+x >= 0 and j+y >= 0:
            try:
              cell.neighbors += board[i+x][j+y].mine
            except:
              pass
    return board
  
class Cell:
  def __init__(self, x, y):
    self.row = x
    self.col = y
    self.flag = False
    self.open = False
    self.mine = False
    self.neighbors = 0

