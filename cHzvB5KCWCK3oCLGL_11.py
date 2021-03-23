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

from collections import defaultdict
def game_of_life(board):
  matrix = defaultdict(int)
  imax, jmax = 0, 0
  for j, line in enumerate(board):
    jmax = max(jmax,j)
    for i, char in enumerate(line):
      imax = max(imax,i)
      matrix[(i,j)] = char
  board2 = "\n".join(["".join([next_life((i,j),matrix) for i in range(imax+1)]) for j in range(jmax+1)])
  return board2
​
def next_life(coord, matrix):
  shifts = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  neigbo = sum([matrix[(coord[0]+shift[0],coord[1]+shift[1])] for shift in shifts])
  if matrix[coord] == 1 and (neigbo == 2 or neigbo == 3):
    return "I"
  if matrix[coord] == 0 and neigbo == 3:
    return "I"
  return "_"

