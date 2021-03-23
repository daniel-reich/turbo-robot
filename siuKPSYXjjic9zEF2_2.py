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
​
PI = math.pi
thickness = 0.025 / 10.0
​
def foil(length):
    if length == 0:
        return 4.0
    d = 4.0     # diameter of current layer
    circ = PI * d
    while length >= 0:
        if length >= circ:
            d += 2 * thickness
            length -= circ
        elif length >= 0:
            d += thickness
            length -= .5 * circ
        circ = PI * d
    return round(d, 4)

