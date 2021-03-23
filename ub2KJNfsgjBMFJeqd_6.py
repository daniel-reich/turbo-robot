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
​
    def __init__(self, rows=14, columns=18, mines=40):
        self.rows = rows
        self.cols = columns
        self.mines = mines
        self.board = []
        # determine mine positions randomly:
        mine_pos = []
        while len(mine_pos) < mines:
            r, c = random.randint(0, rows - 1), random.randint(0, columns - 1)
            while (r, c) in mine_pos:
                r, c = random.randint(0, rows - 1), random.randint(0, columns - 1)
            mine_pos.append((r, c))
        # now construct board:
        for r in range(rows):
            row = []
            for c in range(columns):
                cell = Cell(r, c, (r, c) in mine_pos)
                row.append(cell)
                for r2 in range(r - 1, r + 2):
                    for c2 in range(c - 1, c + 2):
                        if (r2, c2) != (r, c) and (r2, c2) in mine_pos:
                            cell.addMineNeighbor()
            self.board.append(row[:])
  
class Cell:
​
    def __init__(self, row, col, mine):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbors = 0
        self.flag = False
        self.open = False
​
    def addMineNeighbor(self):
        self.neighbors += 1

