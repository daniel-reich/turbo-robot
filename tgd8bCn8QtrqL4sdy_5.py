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
  d=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
  return [[grid[i][j]  if grid[i][j]!='?' else str(sum([grid[i+y][j+x]=='#' for x,y in d if 0<=i+y<len(grid) and 0<=j+x<len(grid[0])])) for j in range(len(grid[0]))]for i in range(len(grid))]

