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
def foil(length):
    diam=4
    cir=0
    while length>0:
        cir=pi*diam 
        length-=cir
        diam+=.0050
    return round(diam-.0025*(cir/2+length<0),4)

