"""


Given a 2D array of mines, replace the **question mark** with the number of
mines that immediately surround it. This includes the diagonals, meaning it is
possible for it to be surrounded by **8 mines maximum**.

The key is as follows:

  * An empty space: **"-"**
  * A mine: **"#"**
  * Number showing number of mines surrounding it: **"?"**

###  Examples

    minesweeper([
      ["-", "#", "-"],
      ["-", "?", "-"],
      ["-", "-", "-"]
    ]) ➞ [
      ["-", "#", "-"],
      ["-", "1", "-"],
      ["-", "-", "-"]
    ]
    
    minesweeper([
      ["-", "#", "-"],
      ["#", "-", "?"],
      ["#", "#", "-"]
    ]) ➞ [
      ["-", "#", "-"],
      ["#", "-", "2"],
      ["#", "#", "-"]
    ]
    
    minesweeper([
      ["-", "#", "#"],
      ["?", "#", ""],
      ["#", "?", "-"]
    ]) ➞ [
      ["-", "#", "#"],
      ["3", "#", ""],
      ["#", "2", "-"]
    ]
    
    minesweeper([
      ["-", "-", "#"],
      ["?", "-", "-"],
      ["-", "-", "-"]
    ]) ➞ [
      ["-", "-", "#"],
      ["0", "-", "-"],
      ["-", "-", "-"]
    ]

### Notes

  * You will only be given **3x3** grids.
  * The question mark is not limited to the centre (there may be multiple question marks).

"""

flatten = lambda l: [i for sl in l for i in sl]
zero_out = lambda l: [['0' if i == '?' else i for i in sl] for sl in l]
​
# Get surrounding elements of an element in (i,j) of 2D grid
get_surround = lambda l, i, j: [sl[j-1 if j else 0:j+2] for sl in l[i-1 if i else 0:i+2]]
​
def minesweeper(grid):
  if "?" not in flatten(grid):
    return grid
  if "#" not in flatten(grid):
    return zero_out(grid)
    
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '?':
          grid[i][j] = str(flatten(get_surround(grid, i, j)).count('#'))
      
  return grid

