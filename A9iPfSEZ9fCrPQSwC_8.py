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
  radius=float(radius)
  coords = []
  total=0
  for point in points:
    for v in point.values():
      coords.append(v)
  for i in range (0, len(coords), 2):
    x1=coords[i]
    y1=coords[i+1]
    x2=centerX
    y2=centerY
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    #print (d, radius, total)
    if d<radius:
      total+=1
  return total

