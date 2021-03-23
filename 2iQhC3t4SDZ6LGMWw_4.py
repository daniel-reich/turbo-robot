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
    if len(points) < 3:
        return True
    X = [p[0] for p in points]
    Y = [p[1] for p in points]
    x_max, x_min, y_max, y_min = max(X), min(X), max(Y), min(Y)
    X_inner = [p for p in points if x_min < p[0] < x_max]
    if len(X_inner) > 0 and not all([p[1] in [y_min, y_max] for p in X_inner]):
        return False
    Y_inner = [p for p in points if y_min < p[1] < y_max]
    if len(Y_inner) > 0 and not all([p[0] in [x_min, x_max] for p in Y_inner]):
        return False
    return True

