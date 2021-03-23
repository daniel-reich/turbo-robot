"""


You have a list of integers, and for each index you want to find the product
of every integer **except the integer at that index**.

Create a function that takes a list of integers and returns a list of the
products.

### Examples

    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 2, 3, 0, 5]) ➞ [0, 0, 0, 30, 0]

### Notes

You can't use division, otherwise you might end up dividing by 0 and the
universe would end.

"""

from functools import reduce
from operator import mul
​
def get_products(lst):
  i=0
  prods = []
  while i<len(lst):
    c = lst[i]
    t = [n for n in lst if n!=c]
    prods.append(reduce(mul, t))
    i+=1
  return prods

