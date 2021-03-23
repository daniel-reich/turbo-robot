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

def foil(l):
  pi=3.1402
  fluidfoil=((0.0025*l/pi+4)**.5)*2
  ex=(fluidfoil)%0.0025
  realfoil=fluidfoil-ex+(0.0025 if ex else 0)
  return round(realfoil,4)

