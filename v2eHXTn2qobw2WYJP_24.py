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

nbrs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
​
def minesweeper_numbers(board):
  size = len(board)
  is_mine = lambda r, c: size>r>=0 and size>c>=0 and board[r][c]==1
  mines = lambda r, c: len(list(filter(bool, [is_mine(r+dr, c+dc) for dr, dc in nbrs])))
​
  return [[9 if board[r][c] == 1 else mines(r, c) for c in range(size)] for r in range(size)]

