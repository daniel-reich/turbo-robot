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
    def __init__(self, row=14, columns=18, mines=40):
        self.rows = row
        self.cols = columns
        self.mines = mines
        self.board = [[Cell(x, y) for y in range(columns)]for x in range(row)]
        a = 0
        for x in self.board:
            for y in x:
                if a != self.mines:
                    y.mine = True
                    a += 1
                else:
                    break
        # update neighbors
        moves = [(1,0), (0,1), (-1,0), (0,-1), (-1, -1), (1,1), (-1, 1), (1, -1)]
        for x in range(self.rows):
            for y in range(self.cols):
                self.board[x][y].neighbors = sum([self.board[x+a][y+b].mine == True for a, b in moves if 0 <= a+x < self.rows and 0 <= b+y < self.cols])
​
class Cell:
    def __init__(self, row, col, mine=False, flag=False, open=False, neighbors=0):
        self.row = row
        self.col = col
        self.mine =  mine
        self.flag = flag
        self.open = open
        self.neighbors = neighbors

