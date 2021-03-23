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
  b = board
  for x in range(0, len(b)):
    for y in range(0, len(b[x])):
      if b[x][y] == 1:
        b[x][y] = 9
  for x in range(0, len(b)):
    for y in range(0, len(b[x])):
      if b[x][y] == 0:
        bombs = 0
        for x2 in range(-1, 2):
          for y2 in range(-1, 2):
            if x + x2 >= 0 and x + x2 < len(b) and y + y2 >= 0 and y + y2 < len(b[0]) and b[x + x2][y + y2] == 9:
              bombs += 1
        b[x][y] = bombs
  return b
