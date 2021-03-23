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

#brute force ftw
from itertools import combinations as c
​
def max_product(lst):
  return max(x*y*z for x,y,z in c(lst,3))
​
def min_product(lst):
  return min(x*y*z for x,y,z in c(lst,3))

