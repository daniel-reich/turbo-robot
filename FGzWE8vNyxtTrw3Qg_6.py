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

class Map:
  class Space:
​
    def __init__(self, val, row, col, maxrow, maxcol):
      self.v = val
      self.r = row
      self.c = col
​
      self.left = None
      self.right = None
      self.top = None
      self.bottom = None
​
      if self.c != 0:
        self.left = '{},{}'.format(self.r, self.c - 1)
      if self.c != maxcol:
        self.right = '{},{}'.format(self.r, self.c + 1)
      if self.r != 0:
        self.top = '{},{}'.format(self.r - 1, self.c)
      if self.r != maxrow:
        self.bottom = '{},{}'.format(self.r + 1, self.c)
​
      self.region = None
  
  def __init__(self, grid):
    self.grid = grid
    self.spaces = {}
​
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        self.spaces['{},{}'.format(r,c)] = Map.Space(grid[r][c], r, c, len(grid) - 1, len(grid[0]) - 1)
  
  def grow_region(self, start, region_number):
​
    nearby_spaces = [space for space in [self.spaces[start].left, self.spaces[start].right, self.spaces[start].top, self.spaces[start].bottom] if space != None]
​
    ns = [self.spaces[space] for space in nearby_spaces if self.spaces[space].v == 1]
​
    if self.spaces[start].region == None:
      self.spaces[start].region = region_number
    
    for space in ns:
      if space.region == None:
        self.grow_region('{},{}'.format(space.r, space.c),region_number)
    
    return True
​
  def count_regions(self):
    
    regions = 0
​
    for r in range(len(self.grid)):
      for c in range(len(self.grid[0])):
        sid = '{},{}'.format(r, c)
        space = self.spaces[sid]
​
        if space.v == 1 and space.region == None:
          regions += 1
          self.grow_region(sid, regions)
    
    return regions
​
​
def num_regions(grid):
  mp = Map(grid)
  return mp.count_regions()

