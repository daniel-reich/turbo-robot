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
  x_values = list(map(lambda x: x[0],points))
  y_values = list(map(lambda x: x[1],points))
  return all(list(map(lambda x: x[0] == min(x_values) or x[0] == max(x_values) or x[1] == min(y_values) or x[1] == max(y_values),points)))

