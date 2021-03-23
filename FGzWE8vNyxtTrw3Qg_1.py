"""


The function is given a rectangular matrix consisting of zeros and ones. Count
the number of different regions and return the result. A separate region is a
collection of ones interconnected horizontally and vertically. A region can
have holes in it.

### Examples

    num_regions([
      [1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]) ➞ 1
    num_regions([
      [1, 1, 1, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1]
    ]) ➞ 2
    
    # The region on the upper left looks like a doughnut.
    num_regions([
      [1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 1, 1]
    ]) ➞ 3

### Notes

N/A

"""

def num_regions(grid):
  m,n = len(grid), len(grid[0])
  ans = 0
  
  for i in range(m):
    for j in range(n):
      if grid[i][j]:
        ans += 1
        stack = [(i,j)]
        while stack:
          a,b = stack.pop()
          grid[a][b] = 0
          for (x,y) in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
            if 0<=x<m and 0<=y<n and grid[x][y]:
              stack.append((x,y))
    
  return ans

