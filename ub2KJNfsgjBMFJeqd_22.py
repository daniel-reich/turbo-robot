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
random.randint(1,101)
​
class Game:
  def __init__ (self, rows=14, cols=18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    dirs = {(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)}
    B = {(i,j):[False,0] for j in range(cols) for i in range(rows)}
    c=0
    while c<mines:
      i = random.randint(0,rows-1)
      j = random.randint(0,cols-1)
      if not B[(i,j)][0]:
        B[(i,j)][0]=True
        c+=1
        for (k,l) in dirs:
          if (i+k,j+l) in B: B[(i+k,j+l)][1]+= 1
    self.board = [[Cell(i,j,*B[(i,j)]) for j in range(cols)] for i in range(rows)]
  
class Cell:
  def __init__ (self, row, col, mine, neighbors):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors
​
#The board shoud be a 2-D list with rows sublists with cols instances of Cell.
​
#Cell should have attributes .row and .col 
#(set these to its position on the board), mine (either True or False),
#.flag and .open (set these two to False) 
#as well as an attribute .neighbors, 
#indicating how many of its neighboring cells are mined.

