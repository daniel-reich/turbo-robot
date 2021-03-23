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
  str = ""
  for j in range(len(board[0])):
    str += update_cell(board, 0, j)
  for i in range(1, len(board)):
    str += "\n"
    for j in range(len(board[0])):
      str += update_cell(board, i, j)
  return str
  
def neighbourhood(board, row, column):
  cnt = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i, j) != (0, 0):
        if 0 <= row + i < len(board) and 0 <= column + j < len(board[0]):
          cnt += board[row + i][column + j]
  return cnt
  
def update_cell(board, row, column):
  nbh = neighbourhood(board, row, column)
  if board[row][column] == 1:
    if nbh == 2 or nbh == 3:
      return "I"
    else:
      return "_"
  else:
    if nbh == 3:
      return "I"
    else:
      return "_"

