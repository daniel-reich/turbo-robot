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
  def __init__(self,rows=14,cols=18,mines=40):
    import random
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.lis = random.sample(list(range(self.rows*self.cols)),self.mines)
    self.board = []
    for i in range(self.rows):
      self.board.append([])
      for j in range(self.cols):
        if i*self.cols+j in self.lis:
          mine = True
        else:
          mine = False
        self.board[i].append(Cell(self,i,j,mine))
​
class Cell:
  def __init__(self,GameObj,row,col,mine):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    neigh_rows = [self.row,self.row+1,self.row-1]
    neigh_cols = [self.col,self.col+1,self.col-1]
    self.neighbors = 0
    for i in neigh_rows:
      for j in neigh_cols:
        if (i,j) != (self.row,self.col) and 0 <= i < GameObj.rows and 0 <= j < GameObj.cols:
          if i*GameObj.cols+j in GameObj.lis:
            self.neighbors += 1

