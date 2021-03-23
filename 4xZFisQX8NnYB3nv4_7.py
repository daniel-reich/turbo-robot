"""


Given a list of seats, return the maximum number of new people which can be
seated, as long as there is at least a gap of **2 seats** between people.

  * Empty seats are given as `0`.
  * Occupied seats are given as `1`.
  * Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.

### Examples

    maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) ➞ 2
    # [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    
    maximum_seating([0, 0, 0, 0]) ➞ 2
    # [1, 0, 0, 1]
    
    maximum_seating([1, 0, 0, 0, 0, 1]) ➞ 0
    # There is no way to have a gap of at least 2 chairs when adding someone else.

### Notes

  * Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
  * All seats will be valid.

"""

class Cinema_Row:
  class Space:
​
    def __init__(self, id, occupied = False):
      self.id = id
      self.occ = occupied
    
    def can_fill(self, spaces, dist):
      for n in range(dist+1):
        pn = self.id - n
        nn = self.id + n
​
        try:
          pv = spaces[pn].occ
        #  print(pv)
        except KeyError:
          pv = None
        
        try:
          nv = spaces[nn].occ
        except KeyError:
          nv = None
        
        if pv == True or nv == True:
          return False
      
      self.occ = True
      return True
  
  def __init__(self, row, gap = 2):
    self.r = row
    self.g = gap
    self.spaces = {}
​
    for n in range(len(row)):
      self.spaces[n] = Cinema_Row.Space(n, row[n] == 1)
  
  def fill(self):
​
    ns = []
​
    for sid in sorted(self.spaces.keys()):
      space = self.spaces[sid]
      if space.can_fill(self.spaces, self.g) == True:
        ns.append(1)
      else:
        if space.occ == False:
          ns.append(0)
        else:
          ns.append(1)
    
    return ns
​
  def compare_orig(self):
​
    ones = 0
​
    for space in self.spaces.values():
      if space.occ == True:
        ones += 1
    
    orig_ones = self.r.count(1)
​
    return ones - orig_ones
​
​
def maximum_seating(lst):
​
  row = Cinema_Row(lst)
​
  row.fill()
​
  return row.compare_orig()

