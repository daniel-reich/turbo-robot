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

def points_in_circle(points, centerX, centerY, radius):
  def inside(point,x0, y0, r):
    return int((point['x']-x0)**2 + (point['y']-y0)**2 < r**2)  
  
  return sum([inside(i,centerX, centerY, radius) for i in points])

