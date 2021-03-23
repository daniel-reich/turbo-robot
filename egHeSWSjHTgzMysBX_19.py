"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

from fractions import Fraction
def half_a_fraction(fract):
  x = Fraction(fract)
  y = x * Fraction(1,2)
  z = '{}/{}'.format(y.numerator,y.denominator)
  return z

