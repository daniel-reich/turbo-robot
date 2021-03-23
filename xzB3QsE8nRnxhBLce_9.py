"""


Create three functions that will do three things:

  * Multiply one number by the sine of another number.
  * Multiply one number by the COSINE of another number.
  * Multiply one number by the tangent of another number.

In each function, you will be given 2 numbers: `x` and `y`. Another important
thing to note, the numbers will be in **degrees** , not **radians**. That is
**extremely important**. Remember to round the result to 2 decimal places, as
well.

### Examples

    sine(8, 27) ➞ 8 sin 27 ➞ 3.63
    
    cosine(10, 4) ➞ 10 cos 4 ➞ 0.70
    
    tangent(4, 39) ➞ 4 tan 39 ➞ 2.52

### Notes

  * The math module will be given to you in the code.
  * Follow my Instagram: _@thatpythoncoder_

"""

from math import sin as s
from math import cos as c
from math import tan as t
from math import radians as r
from math import degrees as d
​
def sine(x, y):
  return round(x * s(r(y)), 2)
​
def cosine(x, y):
  return round(x * c(r(y)), 2)
​
def tangent(x, y):
  return round(x * t(r(y)), 2)

