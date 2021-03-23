"""


[Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) is a two-
dimensional Turing machine invented in the late 1980s. The ant starts out on a
grid of black and white cells and follows a simple set of rules that has
complex emergent behavior.

![Langton's ant](https://edabit-
challenges.s3.amazonaws.com/LangtonsAntAnimated.gif)

The ant can travel in any of the four cardinal directions on each step. The
ant moves according to the following rules:

  * At a white square (1), turn 90° right, flip the color of the square, and move forward one unit.
  * At a black square (0), turn 90° left, flip the color of the square, and move forward one unit.
  * The grid has no limits and therefore if the ant moves outside the borders, the grid should be expanded with 0s, respectively maintaining the rectangle shape.

Create a function **Langton's Ant** with the following parameters:

    grid - a two-dimensional list of 1s and 0s
    # representing white and black cells respectively
    
    column - horizontal position of the ant
    
    row - ant's vertical position
    
    n - number of iterations
    
    direction - ant's current direction
    # 0 - north, 1 - east, 2 - south, 3 - west
    # default value will be 0

... and returns the **state** of the grid after `n` iterations.

### Examples

    langtons_ant([[1]], 0, 0, 1, 0) ➞ [[0, 0]]
    # Initially facing north (0), at the first iteration the ant turns
    # right because it stands on a white square, 1. After that, it flips
    # the square and moves forward.
    
    langtons_ant([[0]], 0, 0, 1, 0) ➞ [[0, 1]]
    
    langtons_ant([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2, 10, 1) ➞ [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]

### Notes

N/A

"""

def langtons_ant(grid, x, y, n, d=0):
  for i in range(n):
    if d==0:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d=3
    elif d==1:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d-=1
    elif d==2:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d-=1
    elif d==3:
      if grid[x][y]==1:
        d=0
      elif grid[x][y]==0:
        d-=1
    grid,x,y = move(grid,x,y,d)
  return grid
        
def move(grid,x,y,d):
  if d==0:
    a,b = -1,0
  elif d==1:
    a,b = 0,1
  elif d==2:
    a,b = 1,0
  elif d==3:
    a,b = 0,-1
  if grid[x][y]==1: grid[x][y]=0
  else: grid[x][y]=1
  if 0<=x+a<len(grid) and 0<=y+b<len(grid[x]):
    return grid,x+a,y+b
  elif x+a<0:
    grid = ([[0] * len(grid[x])])+grid
    return grid,x,y
  elif x+a==len(grid):
    grid = grid + ([[0] * len(grid[x])])
    return grid,x+a,y+b
  elif y+b<0:
    grid = [[0]+i for i in grid]
    return grid,x,y
  elif y+b==len(grid[x]):
    grid = [i+[0] for i in grid]
    return grid,x+a,y+b

