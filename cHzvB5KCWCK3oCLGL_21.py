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
  result = [[] for x in board]
  poss = [(1,1), (0,1), (1,0), (-1,1), (1,-1), (-1,-1), (0,-1), (-1,0)]
  for i in range(len(board)):
    for j in range(len(board[i])):
      empty, filled = 0, 0
      for k in poss:
        if i+k[0] >= 0 and i+k[0] < len(board) and j+k[1] >=0 and j+k[1] < len(board[0]):
          if board[i+k[0]][j+k[1]] == 1: filled +=1 
          else: empty += 1
      if board[i][j] == 0 and filled == 3: result[i].append("I")
      elif board[i][j] == 1 and (filled == 2 or filled == 3): result[i].append("I")
      else: result[i].append("_")
  return "\n".join(["".join(x) for x in result])

