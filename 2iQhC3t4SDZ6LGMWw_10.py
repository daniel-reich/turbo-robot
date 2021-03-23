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

import operator
def on_rectangle_bounds(points):
    Liste=points
    if int(len(points))<=2:
        return True
    else:
        Xmin=sorted(Liste,key=operator.itemgetter(0))[0][0]
        Xmax=sorted(Liste,key=operator.itemgetter(0))[int(len(sorted(Liste,key=operator.itemgetter(0))))-1][0]
        Ymin=sorted(Liste,key=operator.itemgetter(1))[0][1]
        Ymax=sorted(Liste,key=operator.itemgetter(1))[int(len(sorted(Liste,key=operator.itemgetter(0))))-1][1]
        for p in points:
            if p[0]!=Xmin:
                if p[0]!=Xmax:
                    if p[1]!=Ymin:
                        if p[1]!=Ymax:
                            return False
        return True

