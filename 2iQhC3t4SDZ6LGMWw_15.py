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
  x,y=[points[i][0] for i in range(len(points))],[points[i][1] for i in range(len(points))]
  return sum([1 for i in range(len(points)) \
  if (((points[i][0]== max(x) or points[i][0]==min(x)) and (points[i][1]<=max(y) and points[i][1]>=min(y))) \
  or ((points[i][1]== max(y) or points[i][1]==min(y)) and (points[i][0]<=max(x) and points[i][0]>=min(x))))]) == len(points)

