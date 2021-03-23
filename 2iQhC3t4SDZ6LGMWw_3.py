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
  trans_points = list(zip(*points))
  max_x, min_x = max(trans_points[0]), min(trans_points[0])
  max_y, min_y = max(trans_points[1]), min(trans_points[1])
  for i in points:
    if max_x == i[0] or min_x == i[0] or max_y == i[1] or min_y == i[1]: continue
    else: return False
  return True

