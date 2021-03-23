"""


Given a rectangular grid of m by n spaces, signaled by 0s, and a number of
points, signaled by 1, 2, 3..., return the number of moves for the shortest
path that starts at 1 and goes over all the other points in ascending order.

### Examples

    shortest_path([
      ("001"),
      ("002"),
      ("003")
    ]) ➞ 2
    
    shortest_path([
      ("00000"),
      ("01006"),
      ("02000"),
      ("30050"),
      ("00004")
    ]) ➞ 13
    
    shortest_path([
      ("00020000"),
      ("01000000")
    ]) ➞ 3

### Notes

  * Only horizontal and vertical movements are allowed.
  * All movements from one place to an adjacent one count as 1 regardless of direction.
  * The points range from 1 to at most 9 with no repeating or missing digits.

"""

def shortest_path(lst):
​
  class Space:
​
    def __init__(self, val, row, col, mr, mc):
      self.val = val
      
      self.r = row
      self.c = col
      self.ident = '{}{}'.format(row,col)
​
      self.mr = mr
      self.mc = mc
​
      poss_rows = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      near_rows = []
      near_cols = []
​
      if self.r == 'A':
        near_rows.append('B')
      elif self.r == self.mr:
        near_rows.append(poss_rows[poss_rows.index(self.r) - 1])
      else:
        near_rows.append(poss_rows[poss_rows.index(self.r) - 1])
        near_rows.append(poss_rows[poss_rows.index(self.r) + 1])
      
      if self.c == 0:
        near_cols.append(1)
      elif self.c == self.mc:
        near_cols.append(self.c - 1)
      else:
        near_cols.append(self.c - 1)
        near_cols.append(self.c + 1)
      
      self.nearby = []
​
      for row in near_rows:
        self.nearby.append('{}{}'.format(row, self.c))
      for col in near_cols:
        self.nearby.append('{}{}'.format(self.r, col))
  
    def move_to(self, other):
      if other.ident in self.nearby:
        return 1
      else:
        rows = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        row_diff = abs(rows.index(other.r) - rows.index(self.r))
        col_diff = abs(other.c - self.c)
        return row_diff + col_diff
  
​
  spaces = []
  
  rows = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  rindex = 0
​
  for item in lst:
    for col in range(len(item)):
      spaces.append(Space(int(item[col]), rows[rindex], col, len(lst), len(item)-1))
    rindex += 1
  
  values = {}
​
  for space in spaces:
    if space.val > 0:
      values[space.val] = space
  
  distances = []
​
  for k in sorted(values.keys()):
    try:
      distances.append(values[k].move_to(values[k+1]))
    except KeyError:
      continue
  
  return sum(distances)

