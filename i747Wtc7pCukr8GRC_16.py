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

def max_product(lst):
  lst.sort()
  if lst[0] * lst[1] * lst[-1]> lst[-1] * lst[-2] * lst[-3]:
    return lst[-1] * lst[0] * lst[1]
  
  return lst[-1] * lst[-2] * lst[-3]
  
​
def min_product(lst):
  lst.sort()
  if lst[-1] * lst[-2] * lst[0] < lst[1] * lst[2] * lst[0]:
    return lst[-1] * lst[-2] * lst[0]
  return lst[1] * lst[2] * lst[0]

