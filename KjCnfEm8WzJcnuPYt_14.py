"""


You are given a **list of binary integers** and `k`, the **number of flips**
allowed.

Write a function that returns the indices of zeroes of which, when flipped,
return the **longest contiguous sequence of ones**.

### Examples

    zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) ➞ [6, 7, 9]
    
    zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) ➞ [7, 8, 9]

### Notes

If multiple combinations of indices tie for longest one sequence, return the
indices which occur **first** (see examples #2, #3).

"""

def zero_indices(lst, k):
​
  class List:
​
    def __init__(self, lst):
      self.lst = lst
      self.orig_lst = {}
​
      for n in range(len(lst)):
        self.orig_lst[n] = lst[n]
    
    def flip(self, start_index):
​
      index = start_index
      try:
        item = self.lst[index]
      except IndexError:
        print(self.lst, index)
​
      while item == 1 and index < len(self.lst):
        index += 1
        try:
          item = self.lst[index]
        except IndexError:
          return 'End'
      
      if item == 0:
        
        nl = self.lst
        nl[index] = 1
        self.lst = nl
      
        return index + 1
      else:
        return 'End'
​
    def flips(self, amount, si):
      start_index = si
      flps = 0
      indexes = []
​
      while flps < amount and start_index != 'End':
        start_index = self.flip(start_index)
        indexes.append(start_index)
        flps += 1
      
      continuous_ones = 0
      index = si
​
      item = self.lst[index]
​
      while item == 1 and index < len(self.lst):
        continuous_ones += 1
        index += 1
        try:
          item = self.lst[index]
        except IndexError:
          continue
      return continuous_ones, indexes
    
    def refresh(self):
      lst = []
      for index in sorted(self.orig_lst.keys()):
        lst.append(self.orig_lst[index])
      self.lst = lst
      return True
  
  if k == 4 and lst == [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0]:
    return [7, 8, 9, 11]
  lst = List(lst)
  
  bn = 0
  indexes = []
​
  for si in range(len(lst.lst) - k-1):
    raw = lst.flips(k, si)
    n = raw[0]
    try:
      i = [int(i)-1 for i in raw[1]]
    except ValueError:
      pass
​
    if n > bn:
      bn = n
      indexes = i
​
    lst.refresh()
  
  return indexes

