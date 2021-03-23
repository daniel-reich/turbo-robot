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
  w=len(board[0])+2
  h=len(board)+2
  board = [[0]*w] + [[0]+row+[0] for row in board] + [[0]*w]
  ans=''
  for i in range(1, h-1):
      for j in range(1, w-1):
          active = sum(board[i+di][j+dj] for di in (-1,0,1) for dj in (-1,0,1) if di or dj)
          ans += "_I"[3 - board[i][j] <= active <= 3]
      ans += '\n'
  return ans[:-1]

