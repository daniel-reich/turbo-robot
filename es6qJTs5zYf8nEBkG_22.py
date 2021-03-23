"""


Create a function that determines whether four coordinates properly create a
rectangle. A rectangle has 4 sides and has 90 degrees for each angle.
Coordinates are given as strings containing an x- and a y- coordinate: `"(x,
y)"`.

For this problem, assume none of the rectangles are tilted.

    is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)", "(1,1)"]) ➞ True

### Examples

    is_rectangle(["(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"]) ➞ True
    
    is_rectangle(["(0, 0)", "(0, 1)"]) ➞ False
    # A line is not a rectangle!
    
    is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)"]) ➞ False
    # Neither is a triangle!
    
    is_rectangle(["(0, 0)", "(9, 0)", "(7, 5)", "(16, 5)"]) ➞ False
    # A parallelogram, but not a rectangle!

### Notes

  * A square is also a rectangle!
  * A parallelogram is NOT necessarily a rectangle (the rectangle is a special case of a parallelogram).
  * If the input is fewer than or greater than 4 coordinates, return `False`.

"""

import re
def is_rectangle(coordinates):
  if len(set(coordinates)) != 4:
    return False
​
  for i in range(len(coordinates)):
    temp = re.findall(r'-{,}\d+',coordinates[i])
    coordinates[i] = (int(temp[0]), int(temp[1]))
  
  cx = sum(coord[0] for coord in coordinates)/4
  cy = sum(coord[1] for coord in coordinates)/4
  center = (cx,cy)
  distances = [distance(coord,center) for coord in coordinates]
  return all(x == distances[0] for x in distances)
​
​
def distance(corner,center):
  dx = (corner[0] - center[0])**2
  dy = (corner[1] - corner[1])**2
  return (dx + dy)**0.5

