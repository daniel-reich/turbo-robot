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

def simple_pair(lst, n):
  count1 = 0  
  count2 = 0
  for x in lst:
    if x == 0 or n % x != 0:
      count1 += 1
      continue
    else:
      y = int(n / x)
    for z in lst:
      if count1 != count2:
        if z == y:
          return [x, z]
      count2 += 1
    count2 = 0
    count1 += 1
  return None

