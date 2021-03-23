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

def game_of_life(board):
  h, w = len(board), len(board[0])
  bounded_get = lambda i, j: board[i][j] if (i >= 0 and i < h and j >= 0 and j < w) else 0
  def count_neighbors(i, j):
    return sum([bounded_get(i - 1 + (k // 3), j - 1 + (k % 3)) for k in range(9)]) - board[i][j]
  
  out = []
  for i in range(h):
    out.append([])
    for j  in range(w):
      n = count_neighbors(i, j)
      oc = '_'
      if board[i][j]:
        if n == 2 or n == 3:
          oc = 'I'
      elif n == 3:
          oc = 'I'
      out[i].append(oc)
  return '\n'.join([''.join(row) for row in out])

