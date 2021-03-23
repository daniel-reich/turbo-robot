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

def minesweeper_numbers(bd):
    for r in range(len(bd)):
        for c in range(len(bd[0])):
            if bd[r][c] == 1:
                bd[r][c] = 9
                
    for r in range(len(bd)):
        for c in range(len(bd[0])):
            if bd[r][c] == 0:
                bd[r][c] = f(bd, r, c)
    return bd
​
def f(b, x , y):
    cnt = 0
    for x, y in [(x-1, y-1), (x-1, y), (x-1, y+1),
                 (x+1, y-1), (x+1, y), (x+1, y+1),
                 (x, y-1), (x, y+1)]:
        cnt += is_mine(b, x, y)
    return cnt
​
def is_mine(b, x, y):
    if (0 <= x < len(b) and
        0 <= y < len(b) and
        b[x][y] == 9):
        return 1
    return 0

