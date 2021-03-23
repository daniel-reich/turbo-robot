"""


This is a sequel to [Chain Reaction (Part
#1)](https://edabit.com/challenge/bf3QRDxH9Ns2SZWZw), with the same setup, but
a different flavor.

As in the previous part, you will be given a rectangular array representing a
"map" with three types of spaces:

  * "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  * "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that
need to be set off for all bombs to be destroyed by the chain reaction**.

Let's look at some examples:

    [
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]

For the map above, the answer is `2`; to explode all bombs you just need to
set off one "+" bomb in the right cluster and one in the left cluster.

    [
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]

For the map above, the answer is `3`; clearly setting off the three bottom "x"
bombs is enough, and no less than three bombs suffice.

    [
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]

For the map above, the answer is `3`; setting off the three rightmost bombs in
the middle row will do the trick.

### Examples

    min_bombs_needed([
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]) ➞ 2
    
    min_bombs_needed([
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]) ➞ 3
    
    min_bombs_needed([
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]) ➞ 3

### Notes

  * Note that both "+" and "x" bombs have an "explosion range" of 1.
  * To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be [part 3](https://edabit.com/challenge/LLieA2XafALFxXRT5)!
  * Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.

"""

class Grid:
  class Space:
​
    def __init__(self, r, c, mr, mc, bomb_typ = '0'):
      self.r = r
      self.c = c
      self.bt = bomb_typ
​
      self.left_near = None
      self.left_up = None
      self.left_down = None
​
      self.up = None
      self.down = None
​
      self.right_near = None
      self.right_up = None
      self.right_down = None
​
      if self.c != 0:
        self.left_near = '{},{}'.format(self.r, self.c-1)
        if self.r != 0:
          self.left_up = '{},{}'.format(self.r - 1, self.c - 1)
        if self.r != mr:
          self.left_down = '{},{}'.format(self.r + 1, self.c - 1)
      
      if self.c != mc:
        self.right_near = '{},{}'.format(self.r, self.c + 1)
        if self.r != 0:
          self.right_up = '{},{}'.format(self.r - 1, self.c + 1)
        if self.r != mr:
          self.right_down = '{},{}'.format(self.r + 1, self.c + 1)
      
      if self.r != 0:
        self.up = '{},{}'.format(self.r - 1, self.c)
      if self.r != mr:
        self.down = '{},{}'.format(self.r + 1, self.c)
​
      self.plus_places = [self.up, self.down, self.left_near, self.right_near]
      self.x_places = [self.left_up, self.left_down, self.right_up, self.right_down]
​
      if self.bt in ['+', 'x']:
        self.ignited = False
      else:
        self.ignited = None
    
    def explode(self, spaces):
      if self.ignited == None:
        return False
      elif self.ignited == True:
        return None
      else:
        self.ignited = True
        if self.bt == '+':
          for sid in self.plus_places:
            if sid == None:
              continue
            space = spaces[sid]
            if space.ignited == False:
              space.explode(spaces)
        elif self.bt == 'x':
          for sid in self.x_places:
            if sid == None:
              continue
            space = spaces[sid]
            if space.ignited == False:
              space.explode(spaces)
        return True
  
  def __init__(self, grid):
​
    self.raw = grid
    self.spaces = {}
    self.bombs = []
    self.exploded = []
​
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        sid = '{},{}'.format(r, c)
        space = Grid.Space(r, c, len(grid) - 1, len(grid[0]) - 1, grid[r][c])
        self.spaces[sid] = space
​
        if space.bt in ['+', 'x']:
          self.bombs.append(sid)
​
  def explode_bomb(self, bomb_index):
​
    bomb = self.spaces[self.bombs[bomb_index]]
    t = bomb.explode(self.spaces)
​
    if t != True:
      return False
​
    for bob in self.bombs:
      if self.spaces[bob].ignited == True and bob not in self.exploded:
        self.exploded.append(bob)
    
    return True
​
​
def min_bombs_needed(grid):
​
  grid = Grid(grid)
​
  n = 0
  c = 0
​
  while len(grid.exploded) < len(grid.bombs):
    t = grid.explode_bomb(n)
    n += 1
    if t == True:
      c += 1
  
  return c

