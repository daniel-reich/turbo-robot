"""


Create a class `Sudoku` that takes a **string** as an argument. The string
will contain the numbers of a regular 9x9 sudoku board **left to right and top
to bottom** , with zeros filling up the empty cells.

### Attributes

An instance of the class `Sudoku` will have one attribute:

  * `board`: a list representing the board, with sublits for each **row** , with the numbers as **integers**. Empty cell represented with `0`.

### Methods

An instance of the class `Sudoku` wil have three methods:

  * `get_row(n)`: will return the row in position `n`.
  * `get_col(n)`: will return the column in position `n`.
  * `get_sqr([n, m])`: will return the square in position `n` if only one argument is given, and the square to which the cell in position `(n, m)` belongs to if two arguments are given.

### Example

![Sudoku picture](https://edabit-
challenges.s3.amazonaws.com/sudoku_hard_039.gif)

    game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
    
    game.board ➞ [
      [4, 1, 7, 9, 5, 0, 0, 3, 0],
      [0, 0, 0, 0, 0, 0, 7, 0, 0],
      [0, 6, 0, 0, 0, 7, 0, 0, 0],
      [0, 5, 0, 0, 0, 9, 1, 0, 6],
      [8, 0, 0, 6, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 4, 0, 0],
      [9, 0, 0, 0, 0, 5, 0, 0, 0],
      [0, 0, 0, 4, 3, 0, 0, 0, 0],
      [2, 0, 0, 7, 0, 1, 5, 8, 0]
    ]
    
    game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
    game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
    game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
    game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
    game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

### Notes

  * All positions are indexed to 0.
  * All orders are assigned left to right and top to bottom.

"""

class Sudoku:
​
    n_edge = 9
    n_sqr = 3
​
    def __init__(self, s):
        self.original_str = s
        self.board = []
        self._make_board_()
​
    def _make_board_(self):
        for r in range(Sudoku.n_edge):
            row = [int(self.original_str[c])
                   for c in range(r * Sudoku.n_edge, (r + 1) * Sudoku.n_edge)]
            self.board.append(row)
​
    def get_row(self, row):
        return self.board[row]
​
    def get_col(self, col):
        return [self.board[r][col] for r in range(Sudoku.n_edge)]
​
    def _get_mini_sqr_(self, begin_row, begin_col):
        return [self.board[r][c]
                for r in range(begin_row, begin_row + Sudoku.n_sqr)
                for c in range(begin_col, begin_col + Sudoku.n_sqr)]
​
    def get_sqr(self, *args):
        row = args[0] // Sudoku.n_sqr
        col = args[0] % Sudoku.n_sqr
        if len(args) == 2:
            col = args[1] // Sudoku.n_sqr
        return self._get_mini_sqr_(row * Sudoku.n_sqr, col * Sudoku.n_sqr)

