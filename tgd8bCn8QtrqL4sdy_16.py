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
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x]=='?':
        grid[y][x] = checkLeftRight(grid,y,x)+checkUpDown(grid,y,x)+checkDiag(grid,y,x)
        grid[y][x]=str(grid[y][x])
  return grid
  
def checkLeftRight(grid,y,x):
  ret = 0
  if x>0 and grid[y][x-1]=='#':
    ret+=1
  if x<len(grid[y])-1 and grid[y][x+1]=='#':
    ret+=1
  return ret
​
def checkUpDown(grid,y,x):
  ret = 0
  if y>0 and grid[y-1][x]=='#':
    ret+=1
  if y<len(grid)-1 and grid[y+1][x]=='#':
    ret+=1
  return ret
  
def checkDiag(grid,y,x):
  ret = 0
  if y>0:
    ret+=checkLeftRight(grid,y-1,x)
  if y<len(grid)-1:
    ret+=checkLeftRight(grid,y+1,x)
  return ret

