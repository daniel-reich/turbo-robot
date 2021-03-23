"""


 **Mubashir** needs your help in a simple task of multiplication of elements
in a given list.

Create a function which takes a list of integers `lst` and a positive integer
`k` and returns the **minimum and maximum possible product of k elements**
taken from the list. If enough elements are not available in the list, return
`None`.

### Examples

    product_pair([1, -2, -3, 4, 6, 7], 1) ➞ (-3, 7)
    
    product_pair([1, -2, -3, 4, 6, 7], 2) ➞ (-21, 42)
    # -3*7, 6*7
    
    product_pair([1, -2, -3, 4, 6, 7], 3) ➞ (-126, 168)
    # -3*6*7, 4*6*7
    
    product_pair([1, -2, -3, 4, 6, 7], 7) ➞ None
    # There are only 6 elements in the list

### Notes

N/A

"""

from numpy import prod
​
def product_pair(lst, k):
  if len(lst) < k:
    return None
  lst.sort()
​
  mn, mx = sorted([prod(lst[:k]), prod(lst[-k:])])
  for i in range(k >> 1):
    mn = min(mn, prod(lst[:i*2 + 1] + lst[len(lst) - (k - (i*2 + 1)):]))
    mx = max(mx, prod(lst[:i*2 + 2] + lst[len(lst) - (k - (i*2 + 2)):]))
​
  return mn, mx

