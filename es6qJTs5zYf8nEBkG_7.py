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
from collections import defaultdict
​
pattern = re.compile(r'(-?\d+), *(-?\d+)')
​
def is_rectangle(coordinates):
  x_entries = defaultdict(int)
  y_entries = defaultdict(int)
  for coord_pair_str in coordinates:
    match = pattern.search(coord_pair_str)
    if match is not None:
      x_entries[match.group(1)] += 1
      y_entries[match.group(2)] += 1
  
  for k in x_entries.keys():
    if x_entries[k] != 2:
      return False
  for k in y_entries.keys():
    if y_entries[k] != 2:
      return False
  return True

