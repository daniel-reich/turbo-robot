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

from math import atan2
​
def polygon(lst):
    x, y = zip(*lst)
    x_mid = sum(x)/len(lst)
    y_mid = sum(y)/len(lst)
    lst.sort(key=lambda x: atan2(x[1]-y_mid, x[0]-x_mid))
    
    pairs, total = zip(lst, lst[1:] + lst[:1]), 0
    for [x1, y1], [x2, y2] in pairs:
        total += x1*y2 - y1*x2
    
    return total/2

