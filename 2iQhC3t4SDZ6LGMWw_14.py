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
    x_points, y_points = [], []
​
    for i in range(0, len(points)):
        x_points.append(points[i][0])
        y_points.append(points[i][1])
​
    x_max, x_min = max(x_points), min(x_points)
    y_max, y_min = max(y_points), min(y_points)
​
    for i in range(0, len(points)):
        if points[i][0] == x_max or points[i][0] == x_min:
            if y_max >= points[i][1] >= y_min:
                pass
            else:
                return False
        elif points[i][0] != x_max or points[i][0] != x_min:
            if points[i][1] == y_max or points[i][1] == y_min:
                pass
            else:
                return False
​
    return True

