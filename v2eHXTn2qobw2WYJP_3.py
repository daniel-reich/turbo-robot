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

from collections import defaultdict
def minesweeper_numbers(board):
  cells = {(i,j) : char
            for i, line in enumerate(board)
            for j, char in enumerate(line)}
  cells_e = defaultdict(lambda: 0)
  for coord in cells.keys():
    cells_e[coord] = cells[coord] 
  shifts = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
  res = dict()
  for (coord) in cells.keys():
    if cells[coord] == 1:
      res[coord] = 9
    else:
      res[coord] = sum([cells_e[(coord[0]+shift[0],coord[1]+shift[1])]
       for shift in shifts])
  res2 = []
  for i, line in enumerate(board):
    row =[]
    for j, char in enumerate(line):
      row.append(res[i,j])
    res2.append(row)
  return res2
        
​
​
​
​
print(minesweeper_numbers([
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]))

