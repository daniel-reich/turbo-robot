"""


The function is given a map with `1` representing land, `0` representing
water. A land cell can have four neighbors along its edges. Compute the total
perimeter of shore-lines that are defined by land cells touching water or the
outer edges of the map. Each cell edge has a length equal to `1`. An isolated
cell without neighbors has a total perimeter length of `4`.

### Examples

    islands_perimeter([
      [0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0]
    ]) ➞ 16
    islands_perimeter([
      [1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
    ]), 42)
    islands_perimeter([
      [1, 0]
    ]) ➞ 4

### Notes

N/A

"""

def islands_perimeter(grid):
  
  class Map:
    
    class Land:
      
      def __init__(self, row, col, water_sides = 4):
        self.r = row
        self.c = col
        self.ws = water_sides
      
      def update(self, spaces, mr, mc):
        
        nearby = []
        
        if self.r != 0:
          nearby.append('{},{}'.format(self.r-1, self.c))
        if self.r != mr:
          nearby.append('{},{}'.format(self.r+1, self.c))
        
        if self.c != 0:
          nearby.append('{},{}'.format(self.r, self.c-1))
        if self.c != mc:
          nearby.append('{},{}'.format(self.r, self.c+1))
        
        for space in nearby:
          if spaces[space] == 'L':
            self.ws -= 1
        
        return True
    class Water:
      
      def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def __init__(self, grid):
      self.g = grid
      
      self.mr = len(grid) - 1
      self.mc = len(grid[0]) - 1
      
      self.spaces = {}
      self.land = []
      self.water = []
      
      for r in range(self.mr+1):
        for c in range(self.mc+1):
        # print(r,c)
          val = self.g[r][c]
          if val == 1:
            self.land.append(Map.Land(r,c))
            self.spaces['{},{}'.format(r,c)] = 'L'
          else:
            self.water.append(Map.Water(r,c))
            self.spaces['{},{}'.format(r,c)] = 'W'
      #print(self.spaces.keys())
      for land in self.land:
        land.update(self.spaces, self.mr, self.mc)
    
    def total_perimeter(self):
      return sum([island.ws for island in self.land])
  
  m = Map(grid)
  
  return m.total_perimeter()

