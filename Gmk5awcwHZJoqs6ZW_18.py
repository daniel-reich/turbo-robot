"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

def largest_island(lst):
  rows = len(lst)
  columns = len(lst[0])
  output = []
  numberOfIslands = countIslands(rows,columns,lst,output)
  return max(output)
​
def isValid(r,c,rows,columns,visited,lst):
  if (r >= 0 and c >= 0 and r < rows and c < columns):
    return (not visited[r][c] and lst[r][c] == 1)
​
def DFS(r,c,rows,columns,visited,lst,output,islandLength):
  rowNumbers = [-1,-1,-1,0,0,1,1,1]
  columnNumbers = [-1,0,1,-1,1,-1,0,1]
  visited[r][c] = True
  for i in range(8):
    if (isValid(r + rowNumbers[i], c + columnNumbers[i], rows, columns, visited, lst)):
      islandLength = islandLength + 1
      DFS(r + rowNumbers[i], c + columnNumbers[i], rows, columns, visited,lst,output,islandLength)
  
  output.append(islandLength)
​
def countIslands(rows,columns,lst,output):
  visited = [[False for r in range(columns)]for c in range(rows)]
  count = 0
  for r in range(rows):
    for c in range(columns):
      islandLength = 0
      if visited[r][c] == False and lst[r][c] == 1:
        islandLength = islandLength + 1
        DFS(r,c,rows,columns,visited,lst,output,islandLength)
        count = count + 1
  return count

