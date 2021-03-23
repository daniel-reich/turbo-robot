"""


Create a function that takes a list representation of a Minesweeper board, and
returns another board where the value of each cell is the amount of its
neighbouring mines.

### Examples

The input may look like this:

    [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 1, 0, 0]
    ]

The `0` represents an **empty space** . The `1` represents a **mine**.

You will have to replace each **mine** with a `9` and each **empty space**
with the number of adjacent mines, the output will look like this:

    [
      [1, 9, 2, 1],
      [2, 3, 9, 2],
      [3, 9, 4, 9],
      [9, 9, 3, 1]
    ]

### Notes

  * Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.
  * A wikipedia page explaining how Minesweeper works is available in the **Resources** tab.

"""

def minesweeper_numbers(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        board[i][j] = 9
        
  for i in range(len(board)):
    for j in range(len(board[i])):
      count = 0
      if board[i][j] != 9:
        rightSide = j+1 < len(board[i])
        leftSide = j-1 >= 0
        topSide = i-1 >= 0
        bottomSide = i+1 < len(board)
        if rightSide:
          if board[i][j+1] == 9:
            count += 1
        if leftSide:
          if board[i][j-1] == 9:
            count += 1
        if topSide:
          if board[i-1][j] == 9:
            count += 1
        if bottomSide:
          if board[i+1][j] == 9:
            count += 1
        if topSide and rightSide:
          if board[i-1][j+1] == 9:
            count += 1
        if topSide and leftSide:
          if board[i-1][j-1] == 9:
            count += 1
        if bottomSide and rightSide:
          if board[i+1][j+1] == 9:
            count += 1
        if bottomSide and leftSide:
          if board[i+1][j-1] == 9:
            count += 1
        board[i][j] = count
  return board

