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
  height = len(grid)
​
  for y in range(height):
      for x in range(height):
          el = grid[y][x]
          if el=="?":
              grid[y][x]=0
​
​
  for y in range(height):
      for x in range(height):
          el = grid[y][x]
          if el==0:
              if x>0:
                  if grid[y][x-1]=="#":     #check left
                      grid[y][x]+=1     
              if x<height-1:
                  if grid[y][x+1]=="#":     #check right
                      grid[y][x]+=1   
              if y>0:
                  if grid[y-1][x]=="#":     #check up
                      grid[y][x]+=1     
              if y<height-1:
                  if grid[y+1][x]=="#":     #check down
                      grid[y][x]+=1
              if x>0 and y>0:
                  if grid[y-1][x-1]=="#":   #check north-west
                      grid[y][x]+=1
              if x<height-1 and y>0:
                  if grid[y-1][x+1]=="#":   #check north-east
                      grid[y][x]+=1
              if x>0 and y<height-1:
                  if grid[y+1][x-1]=="#":   #check south-west
                      grid[y][x]+=1
              if x<height-1 and y<height-1:
                  if grid[y+1][x+1]=="#":   #check south-west
                      grid[y][x]+=1
​
  for y in range(height):
      for x in range(height):
          el = grid[y][x]
          if el!="#" and el!="-":
              grid[y][x]=str(el)
​
​
  return grid

