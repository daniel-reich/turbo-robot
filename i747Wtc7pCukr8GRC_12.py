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
  s = sorted(lst)
  return max(s[-1]*s[-2]*s[-3],s[-1]*s[0]*s[1])
​
def min_product(lst):
  s = sorted(lst)
  return min(s[0]*s[1]*s[2],s[0]*s[-1]*s[-2])

