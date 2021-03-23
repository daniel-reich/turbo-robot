"""


Create a function that takes the values `Dd` (Dielectric Outer Diameter), `Dc`
(Inner Conductor Diameter) and `er` (Dielectric Constant) and calculates the
Coaxial Cable Impedance.

### Examples

    impedance_calculator(20.7, 2, 4) ➞ 70.0
    
    impedance_calculator(5.3, 1.2, 2.2) ➞ 60.0
    
    impedance_calculator(4.48, 1.33, 2.2) ➞ 50.0

### Notes

  * If you get stuck on a challenge, find help in the **Resources** tab.
  * Round your result to one decimal place.

"""

import math
def impedance_calculator(Dd, Dc, er):
    return round((138 / (er ** 0.5)) * math.log10(Dd/Dc),1)

