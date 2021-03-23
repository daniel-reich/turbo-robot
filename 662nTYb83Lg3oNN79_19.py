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
    a = ( lst[1][0] - lst[0][0], lst[1][1] - lst[0][1] )
    b = ( lst[2][0] - lst[0][0], lst[2][1] - lst[0][1] )
    c = ( lst[3][0] - lst[0][0], lst[3][1] - lst[0][1] )
    A = a[0] == b[0] + c[0] and a[1] == b[1] + c[1]
    B = b[0] == a[0] + c[0] and b[1] == a[1] + c[1]
    C = c[0] == a[0] + b[0] and c[1] == a[1] + b[1]
    return A or B or C

