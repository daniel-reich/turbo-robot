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
  if len(lst) == 3:
    return lst[0]*lst[1]*lst[2]
  pos = [el for el in lst if el>=0]
  neg = [el for el in lst if el < 0]
  pos.sort()
  neg.sort()
  p1 = -500
  p2 = -500
  if len(pos) == 0:
    p2 = neg[-1]*neg[-2]*neg[-3]
    return p2
  if len(pos) >= 3:
    p1 = pos[-1]*pos[-2]*pos[-3]
  if len(neg) >= 2:
    p2 = neg[0]*neg[1]*pos[-1]
  if p1 >= p2:
    return p1
  else:
    return p2
​
def min_product(lst):
  if len(lst) == 3:
    return lst[0]*lst[1]*lst[2]
  pos = [el for el in lst if el>=0]
  neg = [el for el in lst if el < 0]
  pos.sort()
  neg.sort()
  p1 = 1000
  p2 = 1000
  if len(neg) == 0:
    p2 = pos[-1]*pos[-2]*pos[-3]
    return p2
  if len(neg) >= 3:
    p1 = neg[0]*neg[1]*neg[2]
  if len(pos) >= 2:
    p2 = pos[-1]*pos[-2]*neg[0]
  if p1 <= p2:
    return p1
  else:
    return p2

