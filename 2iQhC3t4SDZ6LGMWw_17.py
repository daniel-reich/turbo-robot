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
  if len(points) <= 2:
    return True
  else:
    y = list(map(lambda x: x[1],points))
    x = list(map(lambda x: x[0],points))
    x1 = min(x)
    x2 = max(x)
    y1 = min(y)
    y2 = max(y)
    for point in points:
      if point[0] != x1 and point[1] != y1 and point[0] != x2 and point[1] != y2:
        return False
    return True

