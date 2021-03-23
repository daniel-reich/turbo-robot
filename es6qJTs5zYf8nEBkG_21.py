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

def is_rectangle(coordinates):
  x = 0
  y = 1
  coords = list(map(lambda x: tuple(map(lambda y: abs(y),eval(x))), coordinates))
  if len(coords) < 4:
    return False
  return (abs(coords[0][x]) == abs(coords[1][x]) and 
          coords[1][y] == coords[2][y] and 
          coords[2][x] == coords[3][x])

