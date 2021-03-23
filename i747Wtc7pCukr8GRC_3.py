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

import itertools
def max_product(lst):
  pos = list(itertools.combinations(lst,3))
  return max([get_product(p) for p in pos])
​
def min_product(lst):
  pos = list(itertools.combinations(lst,3))
  return min([get_product(p) for p in pos])
​
def get_product(nums,res=1):
  for num in nums:
    res *= num
  return res

