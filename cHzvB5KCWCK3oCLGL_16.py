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
  answer = []
  for y in range(len(board)):
    row = []
    for x in range(len(board[y])):
      count = 0
      if (y-1) > -1 and (x -1) > -1 and board[y -1][x - 1] == 1:
          count += 1
      if (y-1) > -1 and board[ y -1][x] == 1:
          count +=1
      if (y -1) > -1 and (x + 1) < len(board[y - 1]) and board[y - 1][ x + 1] == 1:
          count += 1
      if ( x - 1 ) > -1 and board[y][x -1] == 1:
          count += 1
      if board[y][x] == 1:
          count += 1
      if (x + 1) < len(board[y - 1]) and board[y][x + 1] == 1:
          count += 1
      if ( y + 1 ) < len(board) and (x -1 ) > -1 and board[ y +1][x - 1] == 1:
          count += 1
      if ( y + 1 ) < len(board) and board[y + 1][x] == 1:
          count +=1
      if  (y + 1 ) < len(board) and (x + 1) < len(board[y - 1]) and board[y + 1][x + 1] == 1:
          count +=1
      if count < 3 or count > 4 or (count == 4 and board[y][x] == 0):
        row.append("_")
      else:
        row.append("I")
    answer.append(''.join(row) + "\n")
    row.clear()
  return ''.join(answer)[:-1]

