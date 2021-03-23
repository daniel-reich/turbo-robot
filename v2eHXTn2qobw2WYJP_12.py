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
    all_places_to_visit = [(-1, -1), (-1, 1), (-1, 0), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == 1:
                board[row][col] = 9
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] != 9:
                counter = 0
                for x, y in all_places_to_visit:
                    if 0 <= row+x < len(board) and 0 <= col+y < len(board[row]):
                        if board[row+x][col+y] == 9:
                            counter += 1
                board[row][col] = counter
    return board

