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
  length = len(lst)
  for index in range(length):
    if lst[index] != 0 and n % lst[index] == 0:
      quo = n//lst[index]
      if quo in lst[:index] or quo in lst[index+1:]:
        return [lst[index],quo]
  return None

