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

class Cell:
    def __init__(self, row=None, col=None):
        self.row=row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
        self.neighbors = 0
​
class Game:
    def __init__(self, rows=14, cols=18, mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = []
        import random
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                c = Cell(i,j)
                r.append(c)
            self.board.append(r)
        minecount = 0
        while minecount < self.mines:
            i = random.randint(0, self.rows-1)
            j = random.randint(0, self.cols-1)
            if self.board[i][j].mine == False:
                self.board[i][j].mine = True
                minecount += 1
        for i in range(self.rows):
            for j in range(self.cols):
                nbr = 0
                for m in [-1,0,1]:
                    for n in [-1,0,1]:
                        if i+m == i and j+n == j:
                            nbr += 0
                        elif i+m<0 or j+n<0:
                            nbr += 0
                        elif i+m>self.rows-1 or j+n>self.cols-1:
                            nbr += 0
                        else:
                            nbr += self.board[i+m][j+n].mine
                self.board[i][j].neighbors = nbr

