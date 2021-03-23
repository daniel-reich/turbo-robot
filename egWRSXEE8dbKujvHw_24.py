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
  d = ((c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)
  ds2 = d**.5
  if ds2 == 0:
    return True
  l = ((c1[0])**2 - (c2[0])**2 + d) / (2 * ds2)
  return (c1[0] * c1[0]) - (l * l) >= 0

