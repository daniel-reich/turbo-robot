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

from itertools import *
def game_of_life(board):
  nrow, ncol = len(board), len(board[0])
  neighbors = {}
  for i, j in product(range(nrow), range(ncol)):
    neighbors[(i, j)] = []
    for x, y in product((-1, 0, 1), repeat=2):
      if 0<=i+x<nrow and 0<=j+y<ncol and (x,y)!=(0,0):
        neighbors[(i, j)].append((i+x, j+y))
  new_board = [list(row) for row in board]
  for (ci, cj), n in neighbors.items():
    num_alive = sum(board[ni][nj] for ni, nj in n)
    if board[ci][cj] and num_alive < 2: new_board[ci][cj] = '_'
    elif board[ci][cj] and num_alive < 4: new_board[ci][cj] = 'I'
    elif board[ci][cj] and num_alive >= 4: new_board[ci][cj] = '_'
    elif num_alive == 3: new_board[ci][cj] = 'I'
    else: new_board[ci][cj] = '_'
  return '\n'.join(''.join(row) for row in new_board)

