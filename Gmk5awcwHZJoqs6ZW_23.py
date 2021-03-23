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

from itertools import product
​
def get(lst, coord):
  x, y = coord
  return lst[y][x]
​
def get_island(lst, coord, width, height, seen, rtn=None):
  if rtn is None:
    rtn = []
  rtn.append(coord)
  x, y = coord
  neighbours = ((x, y+1), (x, y-1),
    (x+1, y+1), (x+1, y), (x+1, y-1),
    (x-1, y+1), (x-1, y), (x-1, y-1))
  neighbours = [(a,b) for a, b in neighbours
    if (0 <= a < width) and (0 <= b < height)]
  for neighbour in neighbours:
    if neighbour in seen:
      continue
    seen.add(neighbour)
    if not get(lst, neighbour):
      continue
    get_island(lst, neighbour, width, height, seen, rtn)
  return rtn
​
​
def largest_island(lst):
  height = len(lst)
  width = len(lst[0])
  seen = set()
  islands = []
  for coord in product(range(width), range(height)):
    if coord in seen:
      continue
    seen.add(coord)
    if not get(lst, coord):
      continue
    islands.append(get_island(lst, coord, width, height, seen))
  return max(len(island) for island in islands)

