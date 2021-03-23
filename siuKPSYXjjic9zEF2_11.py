"""


Aluminum foil has a thickness of **0.025mm**. A roll is formed by tightly
winding it around a tube with an outside diameter of 4cm. Given the length of
the foil in cm, write a function that returns the diameter of the roll in cm
measured at its thickest point. Round the result to four places.

### Examples

    foil(0) ➞ 4.0
    
    foil(50) ➞ 4.02
    
    foil(4321) ➞ 5.4575
    
    foil(10000) ➞ 6.9175

### Notes

N/A

"""

import math
def foil(length,r = 2,turns = 0):
  length_circ = 2 * math.pi * r
  while length > 0:
    length = length - length_circ
    r += 0.0025
    turns += 1
    length_circ = 2 * math.pi * r
  ans = 4 + 2 * ((turns - 1) * 0.0025)
  if abs(length) / length_circ < 0.5 :
    return round(ans + (0.005),4)
  return round(ans + 0.0025,4)

