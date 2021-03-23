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
def foil(length):
  r = 2
  i = 0
  while length>0:
    length -= r*math.pi
    if i:
      r += .0025
    i = 1-i
  return round(2*r+0.0025*i,4)

