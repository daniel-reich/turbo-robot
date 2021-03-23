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
    A, B, C, D = lst
    return is_parallel(A, B, C, D) + is_parallel(A, C, B, D) + is_parallel(A, D, B, C) >= 2
​
def is_parallel(Pa, Pb, Pc, Pd):
    xa, ya, xb, yb, xc, yc, xd, yd = Pa + Pb + Pc + Pd
    return (xa-xb)*(yc-yd) == (ya-yb)*(xc-xd)

