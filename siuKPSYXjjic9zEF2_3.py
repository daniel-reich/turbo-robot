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

from math import pi
import sys
sys.setrecursionlimit(4000)
​
def foil(length, d=4):
    if length <= 0:
        return round(d - 0.0025,4) if -.5*d*pi > length else round(d, 4)
    else:
        return foil(length - d * pi, d + 0.005)

