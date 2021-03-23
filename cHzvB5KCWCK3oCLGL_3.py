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

def neibours(grid, row, column):
    n = 0
    cells = [[-1, 0], [-1, +1], [0, +1], [+1, +1], [+1, 0], [+1, -1], [0, -1], [-1, -1]]
    for c in cells:
        if row+c[0] in range(len(grid)) and column+c[1] in range(len(grid[0])):
            n += grid[row+c[0]][column+c[1]]
    return n
​
​
def nextgen(old):
    new = [l[:] for l in old]
    for r in range(len(new)):
        for c in range(len(new[0])):
            if neibours(old, r, c) == 3:
                new[r][c] = 1
            elif neibours(old, r, c) not in [2, 3]:
                new[r][c] = 0
​
    return new
​
​
def game_of_life(board):
    return '\n'.join(''.join(['_', 'I'][i] for i in l) for l in nextgen(board))

