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

def on_rectangle_bounds(Points):
    if len(Points)<=2:
        return True
    
    xsort=sorted(Points)
    xmax=xsort[len(Points)-1][0]
    xmin=xsort[0][0]
    
    ysort=sorted(Points , key=lambda Points : Points[1])
    ymax=ysort[len(Points)-1][1]
    ymin=ysort[0][1]
    
    for i in range(len(Points)):
        if Points[i][0]!=xmax:
            if Points[i][0]!=xmin:
                if Points[i][1]!=ymax:
                    if Points[i][1]!=ymin:
                        return False
    return True

