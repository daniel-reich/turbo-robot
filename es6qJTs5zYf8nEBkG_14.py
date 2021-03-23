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

def unpack(point):
    return tuple([int(_) for _ in point.replace('(', '').replace(')', '').split(',')])
​
def is_rectangle(coordinates):
    if len(coordinates) != 4:
        return False
    coords = []
    for c in coordinates:
        coords.append(unpack(c))
    coords.sort()
    if len(set(coords)) != 4:
        return False
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]
    x4, y4 = coords[3]
    return x1 == x2 and x3 == x4 and y1 == y3 and y2 == y4

