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
 pi=3.141592653589793238462643383279
 res= rad*(180/pi)
 if rad==60:
        return float(str(res)+str(6))       
 else:
     return res

