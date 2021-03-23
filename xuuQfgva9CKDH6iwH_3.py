"""


You will be given a matrix representing a field `g` and two numbers `x`, `y`
coordinate.

There are three types of possible characters in the matrix:

  * `x` representing a rock.
  * `o` representing a dirt space.
  * `+` representing a grassed space.

You have to simulate grass growing from the position `(x, y)`. Grass can grow
in all four directions (up, left, right, down). Grass can only grow on dirt
spaces and can't go past rocks.

Return the simulated matrix.

### Examples

    simulate_grass([
      "xxxxxxx",
      "xooooox",
      "xxxxoox"
      "xoooxxx"
      "xxxxxxx"
    ], 1, 1) ➞ [
      "xxxxxxx",
      "x+++++x",
      "xxxx++x"
      "xoooxxx"
      "xxxxxxx"
    ]

### Notes

There will always be rocks on the perimeter

"""

def simulate_grass(g, x, y):
  
  class Lawn:
    class Space:
      
      def __init__(self, t, x, y, mx, my):
        self.t = t
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        
        if self.x == 0:
          nx = [self.x + 1]
        elif self.x == self.mx:
          nx = [self.x - 1]
        else:
          nx = [self.x - 1, self.x + 1]
        
        if self.y == 0:
          ny = [self.y + 1]
        elif self.y == self.my:
          ny = [self.y - 1]
        else:
          ny = [self.y - 1,  self.y + 1]
        
        self.space = '{},{}'.format(self.x, self.y)
        self.nearby = []
        
        for x in nx:
          self.nearby.append('{},{}'.format(x, self.y))
        for y in ny:
          self.nearby.append('{},{}'.format(self.x, y))
              
      def grassify(self):
        if self.t == 'x':
          return False
        elif self.t == 'o':
          self.t = '+'
          return True
        else:
          return None
    
    def __init__(self, grid):
      self.lawn = grid
      self.spaces = {}
      
      for x in range(len(grid)):
        for y in range(len(grid[0])):
          self.spaces['{},{}'.format(x,y)] = Lawn.Space(self.lawn[x][y], x, y, len(grid) - 1, len(grid[0]) - 1)
    
    def start_grass(self, x, y):
      return self.spaces['{},{}'.format(x,y)].grassify()
    
    def spread_grass(self):
      
      spreading = True
      c = 0
      
      while spreading == True and c < 1000:
        grass_spaces = [t for t in self.spaces.values() if t.t == '+']
        spreadable = [self.spaces[i] for s in grass_spaces for i in s.nearby]
        grass_results = [s.grassify() for s in spreadable]
        spreading = True in grass_results
        #print(spreading, grass_results)
        c += 1
      
      return True
    
    def display(self):
      ng = []
      for x in range(len(self.lawn)):
        row = []
        for y in range(len(self.lawn[0])):
          row.append(self.spaces['{},{}'.format(x,y)].t)
        ng.append(''.join(row))
      return ng
  
  lawn = Lawn(g)
  
  lawn.start_grass(x, y)
  lawn.spread_grass()
  
  return lawn.display()

