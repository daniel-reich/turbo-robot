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

def minesweeper_numbers(b):
    res = []
    if b:
        rows, cols = len(b), len(b[0])
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if b[r][c]:
                    res[r][c] = 9
                else:
                    n_neighbors = 0
                    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                                 (1, -1), (1, 0), (1, 1)]:
                        if (0 <= r + i < rows and 0 <= c + j < cols
                                and b[r + i][c + j]):
                            n_neighbors += 1
                    res[r][c] = n_neighbors
    return res

