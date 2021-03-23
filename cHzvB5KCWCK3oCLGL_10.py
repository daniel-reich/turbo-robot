"""


![Conway's Game of Life](https://s3.amazonaws.com/edabit-images/game-of-
life.gif)

The goal of this challenge is to implement the logic used in Conway's Game of
Life. Wikipedia will give a better understanding of what it is and how it
works (check the resources tab above).

### Rules

  *  **For a space that's "populated":**
    * Each cell with 0 or 1 neighbours dies, as if by solitude.
    * Each cell with 2 or 3 neighbours survives.
    * Each cell with 4 or more neighbours dies, as if by overpopulation.
  *  **For a space that's "empty" or "unpopulated":**
    * Each cell with 3 neighbours becomes populated.

### Parameters

`board`: a 2-dimensional list of values 0 to 1.

  * 0 means that the cell is empty.
  * 1 means the cell is populated.

### Return Value

A `string` containing the board's state after the game logic has been applied
once.

    On character: I
    Off character: _

### Notes

  * The string should be divided by newlines `\n` to signal the end of each row.
  * A cell's "neighbours" are the eight cells that are vertically, horizontally and diagonally adjacent to it.

"""

import itertools
def game_of_life(board):
  neighbors = list(itertools.product([0,1,-1],repeat=2))[1:]
  res = [['_' for i in row] for row in board]
​
  for i in range(len(board)):
    for j in range(len(board[i])):
      n = 0
      for r, c in neighbors:
        if 0 <= i+r < len(board) and 0 <= j+c < len(board[i]):
          if board[i+r][j+c] == 1:
            n += 1
      if board[i][j] == 1:
        if n == 2 or n == 3:
          res[i][j] = 'I'
      else:
        if n == 3:
          res[i][j] = 'I'
  
  return '\n'.join([''.join(row) for row in res])

