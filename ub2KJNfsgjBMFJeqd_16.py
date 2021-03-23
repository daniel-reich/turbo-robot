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
    def __init__(self, rows = 14, cols = 18, mines = 40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
​
        self.board = [[Cell(x, y) for y in range(cols)] for x in range(rows)]
​
        c = []
​
        for x in range(rows):
            for y in range(cols):
                c.append([x, y])
​
        random.shuffle(c)
​
        for x in range(mines):
            self.board [c[x][0]][c[x][1]].set_mine(True)
​
        for row in self.board:
            for cell in row:
                cell.set_game(self)
​
    def display(self):
        for x in range(self.rows):
            row = ""
            for y in range(self.cols):
                row += self.board [x][y].get_val() + " "
            print(row)
        
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
​
        self.neighbors = 0
​
    def set_mine(self, mine):
        self.mine = mine
​
    def set_game(self, game):
        rows = game.rows
        cols = game.cols
​
        for a in range(-1, 2):
            for b in range(-1, 2):
                if not ( a == 0 and b == 0 ):
                    if self.row + a >= 0 and self.row + a < rows:
                        if self.col + b >= 0 and self.col + b < cols:
                            if game.board [self.row+a][self.col+b].mine:
                                self.neighbors += 1
​
    def get_val(self):
        if self.mine:
            return "M"
        else:
            return str(self.neighbors)

