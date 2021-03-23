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
    mids = []
    a, b, c, d = lst
    pts = [(a,b), (a,c), (a,d), (c,d), (b,d), (b,c)]
    for p in pts:
        m = get_midpt(p)
        if m in mids:
            return True
        mids.append(m)
    return False
​
def get_midpt(p):
    p1, p2 = p
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2, y1+y2)

