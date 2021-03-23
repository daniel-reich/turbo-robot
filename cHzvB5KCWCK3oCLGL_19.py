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
  row, col = len(board), len(board[0])
  new_board = [['_' for tt in range(col)] for t in range(row)]
  for i in range(row):
    for ii in range(col):
      currState = board[i][ii]
      neighbors = sum([getValOnBoard(board, r, c) 
        for r in range(i-1,i+2)
        for c in range(ii-1,ii+2)
        if (r, c) != (i, ii)
        ])
      if (currState == 0 and neighbors == 3) or (currState == 1 and neighbors in [2, 3]):
        new_board[i][ii] = 'I'
  return '\n'.join([''.join(r) for r in new_board])
​
def getValOnBoard(board, row, col):
  if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
    return 0
  else: 
    return board[row][col]

