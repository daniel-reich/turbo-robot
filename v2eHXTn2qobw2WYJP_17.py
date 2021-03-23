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

def get_bombs(lst, row, col, H, W):
    ans = 0
    for row2 in range(row - 1, row + 2):
        for col2 in range(col - 1, col + 2):
            if 0 <= row2 < H and 0 <= col2 < W and (row, col) != (row2, col2) and lst[row2][col2] == 1:
                ans += 1
    return ans
​
def minesweeper_numbers(board):
    if len(board) == 0:
        return board
    W, H = len(board[0]), len(board)
    ans = [[0 for _ in range(W)] for __ in range(H)]
    for row in range(H):
        for col in range(W):
            if board[row][col] == 1:
                ans[row][col] = 9
            else:
                ans[row][col] = get_bombs(board, row, col, H, W)
    return ans

