"""


 **Mubashir** needs your help to write a simple algorithm of multiplication.

Given an array of integers `lst` and an integer `n`, find out a pair of
numbers `[x, y]` from a given array such that **x * y = n**.

If the pair is not found, return `None`.

### Examples

    simple_pair([1, 2, 3], 3) ➞ [1, 3]
    
    simple_pair([1, 2, 3], 6) ➞ [2, 3]
    
    simple_pair([1, 2, 3], 9) ➞ None

### Notes

N/A

"""

class Array:
  
  def __init__(self, lst):
    self.lst = lst
  
  def find_product(self, product):
    for n in self.lst:
      if n == 0:
        continue
      if product % n == 0:
    #   print(n, product // n)
        if product // n in self.lst:
          if product // n == n:
            if self.lst.count(n) > 1:
              return list(sorted([n, product // n]))
            else:
              continue
          return list(sorted([n, product // n]))
    return None
​
def simple_pair(lst, n):
  
  array = Array(lst)
  
  return array.find_product(n)

