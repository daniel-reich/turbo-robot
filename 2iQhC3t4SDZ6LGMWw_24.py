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
  x0 = min(p[0] for p in points)
  x1 = max(p[0] for p in points)
  y0 = min(p[1] for p in points)
  y1 = max(p[1] for p in points)
  return all( ((x == x0 or x == x1) and (y >= y0 and y <= y1)) or \
              ((y == y0 or y == y1) and (x >= x0 and x <= x1)) \
              for x, y in points )

