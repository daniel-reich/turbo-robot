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

def does_brick_fit(a,b,c, *hole):
  brick = sorted([a, b, c])
  return brick[1] <= max(hole) and brick[0] <= min(hole)

