"""


Given a list of 2D points `[x, y]`, create a function that returns `True` if
those points can be on the _bounds_ of a rectangle, `False` otherwise.

![](https://edabit-challenges.s3.amazonaws.com/fhh2XNW.png)

### Examples

    on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0, 0]]) ➞ True
    
    on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0.5, 0.5]]) ➞ False
    
    on_rectangle_bounds([[0, 1], [10, 0], [10, 1]]) ➞ True
    
    on_rectangle_bounds([[0, 1]]) ➞ True

### Notes

Only rectangles with sides parallel to _x-axis_ and _y-axis_ will be
considered.

"""

def on_rectangle_bounds(points):
  b, t = min(points,key=lambda x: x[1])[1], max(points,key=lambda x: x[1])[1]
  l, r = min(points,key=lambda x: x[0])[0], max(points,key=lambda x: x[0])[0]
​
  for p in points:
    if p[0] in [l,r]:
      if not b <= p[1] <= t:
        return False
    elif p[1] in [b,t]:
      if not l <= p[0] <= r:
        return False
    else:
      return False
  return True

