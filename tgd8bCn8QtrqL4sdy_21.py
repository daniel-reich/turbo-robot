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

def minesweeper(grid):
  for row in range(3):
    for col in range(3):
      if grid[row][col] == '?':
        c = 0
        for i in range(-1, 2):
          for j in range(-1, 2):
            nbr, nbc = row+i, col+j
            if 0 <= nbr < 3 and 0 <= nbc < 3:
              c += grid[nbr][nbc] == '#'
        grid[row][col] = str(c)
  return grid

