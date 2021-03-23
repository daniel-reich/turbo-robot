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
class Game:
    def __init__(self,rows=14,cols=18,mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(r,c) for c in range(self.cols)] for r in range(self.rows)]
        
        n = 0
        while n < self.mines:
            r,c = random.randint(0,self.rows-1),random.randint(0,self.cols-1)
            if not self.board[r][c].mine:
                self.board[r][c].mine = True
                n += 1
​
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0 <= r+x < self.rows and 0 <= c+y < self.cols:
                            self.board[r+x][c+y].neighbors += 1
                self.board[r][c].neighbors -= 1
            
class Cell:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
        self.neighbors = 0

