"""


Given a grid of numbers, return a grid of the **Spotlight Sum** of each
number. The spotlight sum can be defined as the total of all numbers
immediately surrounding the number on the grid, including the number in the
total.

### Examples

    spotlight_map([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [12, 21, 16],
      [27, 45, 33],
      [24, 39, 28]
    ]
    spotlight_map([
      [2, 6, 1, 3, 7],
      [8, 5, 9, 4, 0]
    ]) ➞ [
      [21, 31, 28, 24, 14],
      [21, 31, 28, 24, 14]
    ]
    spotlightMap([[3]]) ➞ [[3]]

### Notes

  * Note that all numbers have a spotlight sum, including numbers on the edges.
  * All inputs will be valid grid (all rows will have the same length).

"""

def sum_sur(x,y, G):
  B=[]
  for k in range(len(G)):
    for l in range(len(G[0])):
      if abs(x-k)<2 and abs(y-l)<2:
        B.append(G[k][l])
  return B      
  
def spotlight_map(grid):
  if grid==[[]]:
    return [[]]
  elif grid==[]:
    return []
  else:
    m=len(grid)
    n=len(grid[0])
    C=[]
    for i in range(m):
      for j in range(n):
        C.append(sum(sum_sur(i,j, grid)))
    return [C[i:i+n] for i in range(0,len(C),n)]

