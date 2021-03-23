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
    def __init__(self, board):
        
        self.board = [Sudoku.split(board[x:x+9]) for x in range(0, len(board), 9)]
​
    def split(word):
        return [int(char) for char in word]  
​
    def get_row(self, number):
        return self.board[number]
    def get_col(self, number):
        return [el[number] for el in self.board]
    
    def get_sqr(self, n, m=None):
        square = []
        brutBoard = sum(self.board, [])
        # for num in [0,3,6,27,30,54,57,60]:
        for i in range (0, len(brutBoard), 27):
            for num in range(i,i+9,3):
                if m is not None:
                    indexNumber = 9*n + m
                    if ((indexNumber>=num and indexNumber<=num+3) or (indexNumber>=num+9 and indexNumber<=num+12) or (indexNumber>=num+18 and indexNumber<=num+20)):
                        bigCellIs = brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21]
                        return bigCellIs
                square.append(brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21])
        return square[n]

