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

def spotlight_map(grid):
  class Grid:
    class Space:
      
      def __init__(self, val, r, c, mr, mc):
        self.v = val
        self.r = r
        self.c = c
        self.mr = mr
        self.mc = mc
        
        if self.r == 0:
          near_rows = [self.r, self.r + 1]
        elif self.r == self.mr:
          near_rows = [self.r - 1, self.r]
        else:
          near_rows = [self.r - 1, self.r, self.r + 1]
        
        if self.c == 0:
          near_cols = [self.c, self.c + 1]
        elif self.c == self.mc:
          near_cols = [self.c - 1, self.c]
        else:
          near_cols = [self.c - 1, self.c, self.c + 1]
        
        self.space = '{},{}'.format(self.r, self.c)
        self.nearby = []
        
        for r in near_rows:
          for c in near_cols:
            s = '{},{}'.format(r,c)
            if s != self.space:
              self.nearby.append(s)
      
      def spotlight_val(self, spaces):
        sv = self.v
        
        for space in self.nearby:
          try:
            sv += spaces[space].v
          except KeyError:
            return False
        
        return sv
    
    def __init__(self, grid):
      self.g = grid     
      self.spaces = {}
      
      for r in range(len(self.g)):
        for c in range(len(self.g[0])):
          self.spaces['{},{}'.format(r,c)] = Grid.Space(self.g[r][c], r, c, len(self.g) - 1, len(self.g[0]) - 1)
    
    def spotlight(self):
      
      ng = []
      
      for r in range(len(self.g)):
        row = []
        for c in range(len(self.g[0])):
          space = self.spaces['{},{}'.format(r,c)]
          row.append(space.spotlight_val(self.spaces))
        if False in row:
          return self.g
        ng.append(row)
      
      return ng
  
  grid = Grid(grid)
  
  return grid.spotlight()

