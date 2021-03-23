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

# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
import math
def does_brick_fit(a,b,c, w,h):
  if max(a,b,c)==c:
    return math.sqrt(a**a+b**b)<= math.sqrt(w**w+h**h)
  if max(a,b,c)==b:
    return math.sqrt(a**a+c**c)<= math.sqrt(w**w+h**h)
  else:
    return math.sqrt(c**c+b**b)<= math.sqrt(w**w+h**h)

