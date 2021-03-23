"""


A **complete bracelet** is a list with at least one subsequence (pattern)
repeating _at least two times_ , and _completely_ \- the subsequence cannot be
cut-off at any point. The subsequence **must have length two or greater**.

 **Complete bracelets** :

    [1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]
    
    [1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]
    
    [1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]
    
    [4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]

 **Incomplete bracelets** :

    [1, 2, 2, 2, 1, 2, 2, 2, 1]  # Incomplete (chopped off)
    
    [1, 1, 6, 1, 1, 7]  # Incomplete (subsequence repeats only once)

Create a function that returns `True` if a bracelet is **complete** , and
`False` otherwise.

### Examples

    complete_bracelet([1, 2, 2, 1, 2, 2]) ➞ True
    
    complete_bracelet([5, 1, 2, 2]) ➞ False
    
    complete_bracelet([5, 5, 5]) ➞ False
    # potential pattern [5, 5] cut-off (patterns >= 2)

### Notes

  * Patterns must be at least two integers in length.
  * See **Comments** for a hint if you are stuck.

"""

def complete_bracelet(lst):
  class Bracelet:
​
    def __init__(self, nums):
      self.n = nums
    
    def complete(self, lst, ei):
      n = 0
      
      if len(lst) % len(self.n) == 0:
        while ei != len(lst):
          litem = lst[ei]
          si = self.n[n]
​
          if litem != si:
            return False
        
          n += 1
          if n >= len(self.n):
            n = 0
          
          ei += 1
      
        return True
      else:
        return False
  big_brac_size = int(len(lst) / 2)
​
  bracelets = {}
​
  for n in range(2, big_brac_size + 1):
    l = lst[:n]
    bracelets[n] = Bracelet(l)
  
  for size in bracelets.keys():
    bracelet = bracelets[size]
​
    if bracelet.complete(lst, size) == True:
      return True
    
  return False

