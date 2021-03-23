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

import copy
​
def game_of_life(g):
  results = copy.deepcopy(g)
  rows, columns = len(g), len(g[0])
​
  neighbours = {(-1, 1), (0, 1), (1, 1), (-1, 0), 
        (1, 0), (-1, -1), (0,-1), (1,-1)}
​
  for row in range(rows):
    for col in range(columns):
      value = g[row][col]
      total = 0
      for a, b in neighbours:
         if row + a not in (-1, rows) and col + b not in (-1, columns):
            total += g[row+a][col+b]
      if value == 1 and total not in (2, 3):
        results[row][col] = 0
      elif value == 0 and total == 3:
        results[row][col] = 1
  return '\n'.join(''.join(str(v) for v in row) for row in results).replace('0', '_').replace('1', 'I')

