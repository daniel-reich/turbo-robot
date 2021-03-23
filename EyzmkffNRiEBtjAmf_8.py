"""


Write the function that takes three dimensions of a brick: height(a), width(b)
and depth(c) and returns `True` if this brick can fit into a hole with the
width(w) and height(h).

### Examples

    does_brick_fit(1, 1, 1, 1, 1) ➞ True
    
    does_brick_fit(1, 2, 1, 1, 1) ➞ True
    
    does_brick_fit(1, 2, 2, 1, 1) ➞ False

### Notes

  * You can turn the brick with any side towards the hole.
  * We assume that the brick fits if its sizes equal the ones of the hole (i.e. brick size should be less than or equal to the size of the hole, not strictly less).
  * You **can't** put a brick in at a non-orthogonal angle.

"""

from itertools import *
def does_brick_fit(a,b,c, w,h):
​
  brick = [a, b, c]
  hole = [w, h]
  v, b = hole 
  hole = v * b
  x = list(combinations(brick, 2))
​
  l = []
  for tup in x:
    z, i = tup 
    l.append(z * i)
​
  if hole in l:
    return(True)
  else:
    return(False)

