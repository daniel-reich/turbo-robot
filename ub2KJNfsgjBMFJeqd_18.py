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
​
class Game:
​
    def __init__(self, _rows=14, _cols=18, _mines=40):
        self.rows = _rows
        self.cols = _cols
        self.mines = _mines
        mine_locations, neighbors_count = Game.make_distribution(_rows,
                                                                 _cols,
                                                                 _mines)
        self.board = [[Cell(row, col, mine_locations[row][col] > 0,
                            neighbors_count[row][col])
                       for col in range(_cols)] for row in range(_rows)]
​
    @staticmethod
    def make_distribution(n_rows, n_cols, n_mines):
        res = [[0] * n_cols for _ in range(n_rows)]
        neighbors = [[0] * n_cols for _ in range(n_rows)]
        if n_mines > n_rows * n_cols:
            n_mines = n_rows * n_cols
        mine_idx = set()
        while len(mine_idx) < n_mines:
            mine_idx.add(randint(0, n_rows * n_cols - 1))
        mine_idx = sorted(mine_idx)
        for i in mine_idx:
            res[i // n_cols][i % n_cols] = 1
        for r_idx in range(n_rows):
            for c_idx in range(n_cols):
                neighbors[r_idx][c_idx] = sum(res[x][y] > 0 for x, y in
                                              [(r_idx + i, c_idx + j) for i, j
                                               in
                                               [(i, j) for i in range(-1, 2)
                                                for j in range(-1, 2) if
                                                i or j]]
                                              if 0 <= x < n_rows
                                              and 0 <= y < n_cols)
        return res, neighbors
​
​
class Cell:
​
    def __init__(self, _row=0, _col=0, _mine=False, _neighbors=0):
        self.row = _row
        self.col = _col
        self.mine = _mine
        self.flag = False
        self.open = False
        self.neighbors = _neighbors

