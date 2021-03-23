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
  directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  width = len(lst)
  height = len(lst[0])
  def contiguous_cells(x0,y0):
          if lst[x0][y0] == 1:
              lst[x0][y0] = 0
              adjacent = [(x0 + dx,y0 + dy) for (dx,dy) in directions if 0 <= x0+dx < width and 0 <= y0+dy < height]
              adjacent_ones = [(x,y) for (x,y) in adjacent if lst[x][y] == 1]
              island = [(x0,y0)]
              for cell in adjacent_ones:
                  island = island + contiguous_cells(*cell)
              return island
          return []
  max_size = 0
  for x,row in enumerate(lst):
      for y,cell in enumerate(row):
          if cell:
              max_size = max(max_size, len(contiguous_cells(x,y)))
  return max_size

