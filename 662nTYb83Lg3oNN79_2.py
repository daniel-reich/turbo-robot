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

def is_parallelogram(lst):
    w = sorted(i[0] for i in lst)
    h = sorted(i[1] for i in lst)
    return w[0]-w[2] == w[1]-w[3] and h[0]-h[2] == h[1]-h[3]

