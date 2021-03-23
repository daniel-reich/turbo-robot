"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def half_a_fraction(fract):
  a, b = fract.split('/')
  a, b = int(a), int(b)
  b = b*2 if a%2 else b
  a = a//2 if not a%2 else a
  return '{}/{}'.format(a, b)

