"""


Create a function that takes the length of the side of an equilateral triangle
in centimeters and returns the height of the triangle in millimeters.

### Examples

    height(2) ➞ 17.3 mm
    
    height(5) ➞ 43.3 mm
    
    height(6.2) ➞ 53.7 mm

### Notes

Return the answer rounded to one decimal place and in the format shown in the
examples above.

"""

import math
def height(side):
  string = ""
  height = 1/2 * math.sqrt(3) * side
  height *= 10
  height = round(height, 1)
  string += str(height) + " mm"
  return string

