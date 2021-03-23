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
    self.mine_dist = [1]*mines+[0]*(rows*cols-mines)
    random.seed(3)
    random.shuffle(self.mine_dist)
    self.mine_board = [self.mine_dist[row*cols:(row+1)*cols] for row in range(rows)]
    self.padded = [[0]*(cols+2)]+[[0] + row + [0] for row in self.mine_board]+[[0]*(cols+2)]
    self.neighbor_board = []
    for i in range(1,len(self.padded)-1):
      row = []
      for j in range(1,len(self.padded[i])-1):
        sum = 0
        for (u, v) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
          sum += self.padded[i+u][j+v]
        row.append(sum)
      self.neighbor_board.append(row)
    self.board = [[Cell(row,col,self.mine_board[row][col],self.neighbor_board[row][col]) for col in range(cols)] for row in range(rows)]
class Cell:
  def __init__(self, row, col, mine, neighbors):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors

