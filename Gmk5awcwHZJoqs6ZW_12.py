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
  m = 0
  visited = set()
  nb = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
  
  for i, r in enumerate(lst):
    for j, c in enumerate(r):
      if c and (i, j) not in visited:
        length = 1
        visited.add((i, j))
        stack = [(i, j)]
        
        while stack:
          cr, cc = stack.pop()
          
          for y, x in [(cr+nr, cc+nc) for nr, nc in nb if 0<=cr+nr<len(lst) and 0<=cc+nc<len(lst[0])]:
            if lst[y][x] and (y, x) not in visited:
              visited.add((y, x))
              length += 1
              stack.append((y, x))
              
        m = max((m, length))
  return m

