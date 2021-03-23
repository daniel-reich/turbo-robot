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
  s = fract.split("/")
  integer1 = int(s[0])
  integer2 = int(s[1])
  if integer1 % 2 == 1:
    integer2 = integer2 * 2
  else:
    integer1 = int(integer1 / 2)
  return str(integer1) + "/" + str(integer2)

