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
  dim = 2
  left_up    = [0] * dim
  right_down = [0] * dim
  points_in   = [True] * dim
  points_on   = [True] * dim
  
  for xy in range(dim):
    left_up[xy]    = min(point[xy] for point in points)
    right_down[xy] = max(point[xy] for point in points)
    points_in[xy]   = all(left_up[xy] <= point[xy] 
                     <= right_down[xy] for point in points)
  
  point_on = lambda point: any((point[xy] == left_up[xy])
                           or (point[xy] == right_down[xy])
                           for xy in range(dim))
                           
  points_on = all(point_on(point) for point in points)
  
  return ((points_in == [True, True]) and points_on)

