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

def mag2(p1, p2):
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
​
def is_rectangle(coordinates):
  coords = [[int(x) for x in coord.strip('(').strip(')').split(',')] for coord in coordinates]
  if len(coords) < 4:
    return False
  return mag2(coords[0], coords[1]) == mag2(coords[2], coords[3]) and \
    mag2(coords[1], coords[2]) == mag2(coords[3], coords[0]) and \
    (coords[0][1] - coords[1][1]) * (coords[1][1] - coords[2][1]) == \
    (coords[1][0] - coords[2][0]) * (coords[1][0] - coords[0][0])

