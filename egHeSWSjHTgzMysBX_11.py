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
  fraction = fract.split("/")
  if int(fraction[0]) % 2 == 0:
    return '{}/{}'.format(int(int(fraction[0])/2), int(fraction[1]))
  return '{}/{}'.format(int(fraction[0]), int(fraction[1])*2)

