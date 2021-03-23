"""


In this challenge you will be given a rectangular list representing a "map"
with three types of spaces:

  *  **"+" bombs:** When activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  *  **"x" bombs:** When activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

Consider the grid:

    [
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

    [
      ["1", "2", "0", "x", "6", "8", "0"],
      ["0", "3", "4", "5", "0", "7", "8"]
    ]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the _top
left bomb_ explodes destroys all bombs or not.

### Examples

    all_explode([
      ["+", "+", "+", "+", "+", "+", "x"]
    ]) ➞ True
    
    all_explode([
      ["+", "+", "+", "+", "+", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "0"],
      ["0", "0", "0"],
      ["0", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "x"],
      ["0", "x", "0"],
      ["x", "0", "x"]
    ]) ➞ True

### Notes

  * Both "+" and "x" bombs have an "explosion range" of 1.
  * Part #2 can be [found here](https://edabit.com/challenge/8tDW5gt4SAX2LKALJ).

"""

class Minefield:
  class Space:
    
    def __init__(self, r, c, mr, mc, bomb = False, tp = None):
      self.r = r
      self.c = c
      self.bomb = bomb
      self.tp = tp
      self.exploded = False
      
      self.up_left = None
      self.down_left = None
      self.left = None
      
      if self.c != 0:
        self.left = '{},{}'.format(self.r, self.c - 1)
        if self.r != 0:
          self.up_left = '{},{}'.format(self.r - 1, self.c - 1)
        if self.r != mr:
          self.down_left = '{},{}'.format(self.r + 1, self.c - 1)
      
      self.right = None
      self.up_right = None
      self.down_right = None
      
      if self.c != mc:
        self.right = '{},{}'.format(self.r, self.c + 1)
        if self.r != 0:
          self.up_right = '{},{}'.format(self.r - 1, self.c + 1)
        if self.r != mr:
          self.down_right = '{},{}'.format(self.r + 1, self.c + 1)
      
      self.up = None
      self.down = None
      
      if self.r != 0:
        self.up = '{},{}'.format(self.r-1, self.c)
      if self.r != mr:
        self.down = '{},{}'.format(self.r+1, self.c)
      
      self.cross_near = [space for space in [self.left, self.right, self.up, self.down] if space != None]
      self.x_near = [space for space in [self.up_left, self.up_right, self.down_left, self.down_right] if space != None]
    
    def blow_up(self, spaces):
      
      if self.bomb == True:
        #print(self.r, self.c, self.x_near, self.up_left, self.down_left, self.up_right, self.down_right)
        self.exploded = True
        
        if self.tp == '+':
          to_explode = self.cross_near
        elif self.tp == 'x':
          to_explode = self.x_near
        
        for sid in to_explode:
          if spaces[sid].bomb == True and spaces[sid].exploded == False:
            spaces[sid].blow_up(spaces)
        
        return True
      else:
        return False
  
  def __init__(self, field):
    
    self.field = field
    self.spaces = {}
    
    for r in range(len(field)):
      for c in range(len(field[r])):
        sid = '{},{}'.format(r,c)
        if field[r][c] in ['+','x']:
          space = Minefield.Space(r, c, len(field) - 1, len(field[r]) - 1, True, field[r][c])
        else:
          space = Minefield.Space(r, c, len(field) - 1, len(field[r]) - 1)
        self.spaces[sid] = space
  
  def set_mine_off(self, pos):
    self.spaces[pos].blow_up(self.spaces)
    return True
  
  def count_exploded(self):
    return len([bomb for bomb in self.spaces.values() if bomb.exploded == True])
  
  def count_bombs(self):
    return len([bomb for bomb in self.spaces.values() if bomb.bomb == True])
​
​
def all_explode(grid):
  
  field = Minefield(grid)
  field.set_mine_off('0,0')
  
  return field.count_exploded() == field.count_bombs()

