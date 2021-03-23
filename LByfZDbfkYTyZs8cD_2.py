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

def areaofhexagon(x):
  return round(3**.5*3*x**2*.5,1) if x>0 else None

