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

def points_in_circle(pts, cX, cY, r):
  L2 = lambda a, b: ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5
  return sum(1 for p in pts if L2((p['x'], p['y']), (cX, cY)) < r)

