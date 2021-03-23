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

from itertools import combinations
​
def combos(lst):
  com = []
  for s in combinations(lst, 3):
    if list(s) not in com:
      com.append(list(s))
  for x in range(len(com)):
    com[x] = com[x][0] * com[x][1] * com[x][2]
  return com
​
def max_product(lst):
  lst = combos(lst)
  return max(lst)
​
def min_product(lst):
  lst = combos(lst)
  return min(lst)

