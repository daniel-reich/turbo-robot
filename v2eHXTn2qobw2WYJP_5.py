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
  def digit(i,j):
    if board[i][j] == 1:
      return 9
    total = 0
    for a,b in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
      try:
        if min(a+i,b+j) >= 0:
          if board[a+i][b+j] == 1:
            total += 1
      except IndexError:
        pass
    return total
  return [[digit(i,j) for j in range(0,len(board[0]))] for i in range(0,len(board))]

