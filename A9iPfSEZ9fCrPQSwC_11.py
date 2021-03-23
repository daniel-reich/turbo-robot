"""


Count the amount of coordinates on a two-dimensional grid that are inside a
given circle. The function has four arguments: the points (provided as a list
of dictionaries), the circle's center x, y and the circle's radius.

### Examples

    points_in_circle([
      { "x": 0, "y": 0 },
      { "x": 1, "y": 1 },
      { "x": 0, "y": 5 },
      { "x": 10, "y": 10 }
    ], 0, 0, 5) ➞ 2

### Notes

Only count the coordinates that are _in_ the circle, not the ones that are on
the border.

"""

import math
def points_in_circle(points, centerX, centerY, radius):
  count = 0
  for pt in points:
    dist = math.sqrt((pt['x'] - centerX)**2 + (pt['y'] - centerY)**2)
    if dist < radius: count += 1
  return count

