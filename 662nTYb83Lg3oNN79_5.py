"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

from math import atan2
def is_parallelogram(lst):
    x, y = zip(*lst)
    x_mid = sum(x) / len(lst)
    y_mid = sum(y) / len(lst)
    lst.sort(key=lambda p: atan2(p[1] - y_mid, p[0] - x_mid))
    x, y = zip(*lst)
    sides = [((x[i] - x[(i + 1) % len(x)]) ** 2
              + (y[i] - y[(i + 1) % len(x)]) ** 2) ** 0.5
             for i in range(len(x))]
    return sides[0] == sides[2] and sides[1] == sides[3]

