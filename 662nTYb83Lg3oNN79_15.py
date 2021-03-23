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

import numpy as np
def is_parallelogram(lst):
    cx=lst[0][0]+lst[1][0]+lst[2][0]+lst[3][0]
    cx=float(cx)/4.0
    cy=lst[0][1]+lst[1][1]+lst[2][1]+lst[3][1]
    cy=float(cy)/4.0
    d1=np.square(cx-lst[0][0]) + np.square(cy-lst[0][1])
    d2=np.square(cx-lst[1][0]) + np.square(cy-lst[1][1])
    d3=np.square(cx-lst[2][0]) + np.square(cy-lst[2][1])
    d4=np.square(cx-lst[3][0]) + np.square(cy-lst[3][1])
    m=[d1,d2,d3,d4]
    m=sorted(m)
    #print(m)
    return m[0]==m[1] and m[2]==m[3]

