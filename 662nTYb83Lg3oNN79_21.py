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

from collections import Counter
​
def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2., (p1[1] + p2[1]) / 2.)
​
def is_parallelogram(lst):
    midpoints = []
    for i in range(4):
        for j in range(i + 1, 4):
            midpoints.append(get_midpoint(lst[i], lst[j]))
    C = Counter(midpoints)
    return 2 in C.values() and len(C.keys()) == 5

