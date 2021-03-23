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
  x = dot1[0],dot2[0]
  y = dot1[1],dot2[1]
  xTotal = x[0]-x[1] 
  yTotal = y[0]-y[1] 
    
  c = (xTotal)**2+(yTotal)**2
  cTotal = math.sqrt(c)
  return round(cTotal,2)

