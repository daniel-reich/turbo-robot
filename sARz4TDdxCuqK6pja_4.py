"""


 **Mubashir** needs your help to identify the spread of a deadly virus. He can
provide you with the following parameters:

  * A two-dimensional array `persons`, containing **affected persons 'V'** and **unaffected persons 'P'**.
  * Number of hours `n`, each infected person is spreading the virus to one person _up, down, left and right_ **each hour**.

Your function should return the updated array containing affected and
unaffected persons after `n` hours.

### Examples

    persons = [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    deadly_virus(persons, 0) ➞ [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 1) ➞ [
      ["V", "P", "P", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 2) ➞ [
      ["V", "V", "P", "P", "P"],
      ["V", "V", "V", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]

### Notes

N/A

"""

class City:
  class Person:
    
    def __init__(self, r, c, mr, mc, infected = False):
      self.r = r
      self.c = c
      self.i = infected
      
      if r != 0:
        self.up = '{},{}'.format(r-1, c)
      else:
        self.up = None
      
      if c != 0:
        self.left = '{},{}'.format(r, c-1)
      else:
        self.left = None
      
      if r != mr:
        self.down = '{},{}'.format(r+1, c)
      else:
        self.down = None
      
      if c != mc:
        self.right = '{},{}'.format(r, c+1)
      else:
        self.right = None
      
      self.nearby = [space for space in [self.up, self.down, self.right, self.left] if space != None]
    
    def infect(self, spaces):
      if self.i == True:
        for sid in self.nearby:
          space = spaces[sid]
          if space.i == False:
            space.i = True
      return self.i
  
  def __init__(self, grid):
    self.grid = grid
    self.ppl = {}
    
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        sid = '{},{}'.format(r,c)
        person = City.Person(r, c, len(grid) - 1, len(grid[0]) - 1, grid[r][c] == 'V')
        self.ppl[sid] = person
  
  def hour(self):
    
    infected = [person for person in self.ppl.values() if person.i == True]
    
    for prsn in infected:
      prsn.infect(self.ppl)
    
    return True
  
  def advance_by_hours(self, hours):
    for n in range(hours):
      self.hour()
    return True
  
  def display(self):
    
    tr = []
    
    for r in range(len(self.grid)):
      row = []
      for c in range(len(self.grid[0])):
        sid = '{},{}'.format(r,c)
        person = self.ppl[sid]
        if person.i == True:
          row.append('V')
        else:
          row.append('P')
      tr.append(row)
    
    return tr
​
def deadly_virus(persons, n):
  
  city = City(persons)
​
  city.advance_by_hours(n)
  
  return city.display()

