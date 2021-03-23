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
  new_board = [[0] *len(board[0]) for i in range(len(board))]
  for row in range(len(board)):
    for col in range(len(board[row])):
      neighbors = 0
      if row-1 >= 0:
        neighbors += sum(board[row-1][max(0, col-1):min(col+2, len(board[0]))])
      if row+1 <= len(board)-1:
        neighbors += sum(board[row+1][max(0, col-1):min(col+2, len(board[0]))])
      if col-1 >= 0:
        neighbors+= board[row][col-1]
      if col+1 <= len(board[0])-1:
        neighbors+= board[row][col+1]
      if (board[row][col] == 0 and neighbors == 3) or (board[row][col] == 1 and (neighbors == 2 or neighbors == 3)):
        new_board[row][col] = 1
  return '\n'.join([ ''.join(["I" if num == 1 else "_" for num in row]) for row in new_board])

