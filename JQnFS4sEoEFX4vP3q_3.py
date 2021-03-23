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

import itertools
from functools import reduce
​
def product_pair(lst, k):
  if k > len(lst) or k < 1:
    return None
  elif k == 1:
    return (min(lst),max(lst))
  else:
    newlist = []
    product = 0
    for eachcombo in itertools.combinations(lst,k):
      product = reduce((lambda x,y: x*y),[x for x in eachcombo])
      newlist.append(product)
    return (min(newlist),max(newlist))

