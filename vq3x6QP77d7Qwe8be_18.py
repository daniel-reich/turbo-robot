"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

import numpy as np
def is_odd(npa):
  for i in range(npa.shape[0]):
    for j in range(npa.shape[1]):
      if npa[i,j]%2==0:
        return False
  return True
def odd_square_patch(l2d):
  np2d=np.array(l2d)
  r,c=np2d.shape
  ret=0
  for i in range(r):
    for j in range(c):
      for k in range(1,min(r-i,c-j)+1):
        if k>ret and is_odd(np2d[i:i+k,j:j+k]):
          ret=k
  return ret

