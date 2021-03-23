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
  for i in range(len(lst)):
    #lst2 = lst[i+1:]
    for j in lst[i+1:]:
      first = lst[i]
      second = j
      if check_multiply(first,second,n) == 1:
        return [first,second]
  return None
  
  
def check_multiply(x,y,n):
  if x*y == n:
    return 1
  else:
    return 0

