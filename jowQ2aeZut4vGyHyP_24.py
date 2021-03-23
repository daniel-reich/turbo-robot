"""


Given a slope of a line, calculate and return the value of the angle of line
(relative to the y -axis). For example, a horizontal line would be 90 degrees.

### Examples

    convert(1) ➞ 45
    
    convert(0) ➞ 90
    
    convert(-1) ➞ 135

### Notes

  * All values returned should be in degrees.
  * All values returned should be rounded to the nearest whole number.
  * The value to return must be strictly between 0 and 180.
  * All inputs will be valid integer values.

"""

from math import atan, degrees
​
def convert(slope):
  if slope == 0:
      return 90
  angle = round(degrees(atan(1/slope)))
  if angle < 0:
    return 180 + angle
  return angle

