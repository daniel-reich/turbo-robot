"""


If you have a triangular shape cut from a piece of cardboard, the centroid of
the triangle would be the spot where it balances on the point of a pencil. The
location of the centroid is easy to calculate if you know the `x, y`
coordinates of the vertices:

  * The `x` coordinate of the centroid is at `(x1 + x2 + x3) / 3`
  * The `y` coordinate of the centroid is at `(y1 + y2 + y3) / 3`

`x1, y1, x2, y2, x3, y3` are the coordinates of the three vertices.

Create a function that calculates the position of the centroid given the
coordinates of the vertices. Round the answers to two decimal places. If the
three points given do not form a triangle, return `False`.

### Examples

    centroid(0, 0, 3, 0, 3, 3) ➞ (2.0, 1.0)
    
    centroid(2, 2, 8, -2, 0, -3) ➞ (3.33, -1.0)
    
    centroid(1, 1, 2, 2, 3, 3) ➞ False

### Notes

  * The arguments are given in the order shown above: `x1, y1, x2, y2, x3, y3`.
  * If the three points do not form a triangle, they must lie in a straight line.

"""

import math
def centroid(ax, ay, bx, by, cx, cy):
  ab = round(math.sqrt((bx - ax) ** 2 + (by - ay) ** 2), 1)
  ac = round(math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2), 1)
  bc = round(math.sqrt((cx - bx) ** 2 + (cy - by) ** 2), 1)
  if ab == ac + bc or ac == ab + bc or bc == ab + ac:
    return False
  return (round((ax+bx+cx)/3,2),round((ay+by+cy)/3,2))

