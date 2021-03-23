"""


Given the side length `x` find the area of a hexagon.

![Formula to find the area of a hexagon](https://edabit-
challenges.s3.amazonaws.com/jrfUudjubUBbgU.jpg)

### Examples

    area_of_hexagon(1) ➞ 2.6
    
    area_of_hexagon(2) ➞ 10.4
    
    area_of_hexagon(3) ➞ 23.4

### Notes

  * Return `None` if the side length given is not a positive integer.
  * Round to the nearest tenth.

"""

from math import sqrt
def areaofhexagon(x):
  if x < 0 or x ==0:
    return None
  return round(((3*sqrt(3))/2) * (x**2),1)

