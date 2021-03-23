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

import math
def is_circle_collision(c1, c2):
  return math.sqrt((c2[1]-c1[1])**2+(c2[2]-c1[2])**2) < c2[0] + c1[0]

