"""
Given a **unordered** list of the vertices of a **convex** polygon, find its
area.

### Examples

    polygon([[2, 5], [5, 1], [-4, 3]]) ➞ 15.0
    
    polygon([[-1, 1], [1, 1], [-1, -1], [1, -1]]) ➞ 4.0
    
    polygon([[2, 2], [11, 2], [4, 10], [9, 7]]) ➞ 45.5
    
    polygon([[5, 3], [3, 4], [12, 8], [5, 11], [9, 5]]) ➞ 39.0

### Notes

  * A convex polygon has all interior angles less than 180 degrees.
  * The first example has only 3 vertices so this list is ordered by default.

"""

def polygon(lst):
    # move the list to the first quarter
    xm = min(lst)[0]
    ym = min(lst, key=lambda x: x[1])[1]
    lst = [[L[0] if xm > 0 else L[0] + (-1 * xm), L[1] if ym > 0 else (-1 * ym) + L[1]] for L in lst]
    
    # take the lower left point as reference
    ref = min(lst)
    
    #sort verticies by their angle to reference point
    from math import atan2
    lst.pop(lst.index(ref))
    lst = sorted(lst,key=lambda L:atan2(L[1]-ref[1],L[0]-ref[0]))
    lst.insert(0, ref)
    lst.append(ref)
    
    # general solution area = abs(sum(Xn * Yn+1 - Yn * Xn+1)/2)
    return abs(0.5 * sum([T[0][0] * T[1][1] - T[0][1] * T[1][0] for T in zip(lst, lst[1:])]))

