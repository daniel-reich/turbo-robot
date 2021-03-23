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
    new = [[0 for _ in range(len(board[0]))] for __ in range(len(board))]
    d = [-1, -1, -1, 0, 0, 1, 1, 1]
    e = [-1, 0, 1, -1, 1, -1, 0, 1]
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                new[r][c] = 9
            else:
                mines = 0
                for rr, cc in zip(d, e):
                        if -1 < r + rr < len(board) and -1 < c + cc < len(board[r]):
                            if board[r + rr][c + cc] == 1:
                                mines += 1
                new[r][c] = mines
    return new

