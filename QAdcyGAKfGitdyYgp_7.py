"""


A bacterial culture on day 1 has only one bacterium with mass 1. Every day,
some number of bacteria will split (possibly zero or all). When a bacterium of
mass `m` splits, it becomes two bacteria of mass `m/2` each. Also, every
night, the mass of every bacteria will increase by one.

Write a function that determines the minimum number of nights for the culture
to reach the `final_mass`.

### Examples

    bacteria(9) ➞ 3
    
    # Day 1
    # The bacterium with mass 1 splits. There are now two bacteria with mass 0.5 each.
    
    # Night 1
    # All bacteria's mass increases by one. There are now two bacteria with mass 1.5.
    
    # Day 2
    # None split.
    
    # Night 2
    # There are now two bacteria with mass 2.5.
    
    # Day 3
    # Both bacteria split. There are now four bacteria with mass 1.25.
    
    # Night 3
    # There are now four bacteria with mass 2.25.
    # The total mass is 2.25 + 2.25 + 2.25 + 2.25 = 9.
    # It can be proved that 3 is the minimum number of nights needed.
    # There are also other ways to obtain total mass 9 in 3 nights.
    
    bacteria(16) ➞ 4
    
    bacteria(548) ➞ 9
    
    bacteria(5467) ➞ 12

### Notes

  * This is a simplified version of [D. Phoenix and Science](https://codeforces.com/problemset/problem/1348/D).
  * The input will always be an integer.

"""

class Bacteria_Colony:
  
  def __init__(self, num_of_bact, bact_mass):
    self.nob = num_of_bact
    self.bm = bact_mass
    self.tm = self.nob * self.bm
  
  def grow(self):
    self.bm += 1
    self.tm = self.nob * self.bm
    return True
  
  def split(self):
    self.nob *= 2
    self.bm = self.bm / 2
    self.tm = self.nob * self.bm
    return True
    
​
def bacteria(final_mass):
  
  colony = Bacteria_Colony(1, 1)
  previous_mass = 0
  nights = 0
  
  while colony.tm < final_mass:
    if colony.tm > previous_mass:
      previous_mass = colony.tm
      colony.split()
    # print('split')
    colony.grow()
    nights += 1
    #print(colony.nob, colony.bm, colony.tm)
  
  return nights

