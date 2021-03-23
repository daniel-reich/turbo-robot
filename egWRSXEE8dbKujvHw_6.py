"""


Create a function that returns `True` if the given circles are intersecting,
otherwise return `False`. The circles are given as two lists containing the
values in the following order:

  1. Radius of the circle.
  2. Center position on the x-axis.
  3. Center position on the y-axis.

### Examples

    is_circle_collision([10, 0, 0], [10, 10, 10]) ➞ True
    
    is_circle_collision([1, 0, 0], [1, 10, 10]) ➞ False

### Notes

  * You can expect useable input and positive radii.
  * The given coordinates are the centers of the circles.
  * We are looking for intersecting areas, not intersection outlines.
  * Check the **Resources** tab for help.

"""

def is_circle_collision(c1, c2):
  # create a line
  # if len(line) >= sum of radii, then overlap
  
  c1x = c1[1]
  c1y = c1[2]
  c2x = c2[1]
  c2y = c2[2]
  
  slope = 0
  if c1x - c2x != 0:
    slope = (c1y - c2y) / (c1x - c2x)
  else:
    slope = c1y - c2y
    
  trihyp = 0
  if slope > 0:
    trib = c2x - c1x
    trih = c2y - c1y
    trihyp = (trib**2 + trih **2)**.5
  elif slope < 0:
    trib = c1x - c2x
    trih = c1y - c2y
    trihyp = (trib**2 + trih**2)**.5
  else:
    if c1x > c2x:
      trihyp = c1x - c2x
    else:
      trihyp = c2x - c1x
  
  if c1[0] + c2[0] > trihyp:
    return True
  elif c1[0] + c2[0] < trihyp:
    return False
  else:
    return True

