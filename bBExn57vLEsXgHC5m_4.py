"""


Create a function that returns `True` if three points belong to the same line,
and `False` otherwise. Each point is represented by a list consisting of an x-
and y-coordinate.

### Examples

    same_line([[0, 0], [1, 1], [3, 3]]) ➞ True
    
    same_line([[-2, -1], [2, 1], [0, 0]]) ➞ True
    
    same_line([[-2, 0], [-10, 0], [-8, 0]]) ➞ True
    
    same_line([[0, 0], [1, 1], [1, 2]]) ➞ False
    
    same_line([[3, 4], [3, 5], [6, 6]]) ➞ False

### Notes

Note the special case of a vertical line.

"""

import numpy as np
def same_line(lst):
  x = [point[0] for point in lst]
  y = [point[1] for point in lst]
  
  x2 = x[1::]
  y2 = y[1::]
  unix = np.unique(x)
  uniy = np.unique(y)
  
  if len(unix) == 1 or len(uniy) == 1:
    return True
  elif len(unix) == 2 or len(uniy) == 2:
    return False
  else:
    slopes = [(y1 - y[0])/(x1 - x[0]) for x1, y1 in zip(x2,y2)]
    if slopes[0] == slopes[1]:
      return True
    else:
      return False

