"""


Create a function that takes an angle in radians and returns the corresponding
angle in degrees rounded to one decimal place.

### Examples

    radians_to_degrees(1) ➞ 57.3
    
    radians_to_degrees(20) ➞ 1145.9
    
    radians_to_degrees(50) ➞ 2864.8

### Notes

The number `π` can be loaded from the math module with `from math import pi`.

"""

def radians_to_degrees(rad):
  from math import pi
  x = rad * 180 / pi
  y = round(x,1)
  return y

