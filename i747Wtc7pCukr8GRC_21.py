"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

from itertools import permutations
def max_product(lst):
  perm=permutations(lst,3)
  c=-123234523
  prod=1
  for i in list(perm):
    for d in i:
      prod=prod*d
    if prod>c:
      c=prod
    prod=1
  return c
  
def min_product(lst):
  perm=permutations(lst,3)
  c=123423432
  prod=1
  for i in list(perm):
    for d in i:
      prod=prod*d
    if prod<c:
      c=prod
    prod=1
  return c

