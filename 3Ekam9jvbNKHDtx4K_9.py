"""


Write a function that takes coordinates of two points on a two-dimensional
plane and returns the length of the line segment connecting those two points.

### Examples

    line_length([15, 7], [22, 11]) ➞ 8.06
    
    line_length([0, 0], [0, 0]) ➞ 0
    
    line_length([0, 0], [1, 1]) ➞ 1.41

### Notes

  * The order of the given numbers is X, Y.
  * This challenge is easier than it looks.
  * Round your result to two decimal places.

"""

import math
def line_length(dot1, dot2):
    x1,y1 = dot1
    x2,y2 = dot2
    x = abs(x2-x1)
    y = abs(y2-y1)
    return round(math.sqrt(x**2 + y**2),2)
