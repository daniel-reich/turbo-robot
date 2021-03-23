"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def half_a_fraction(f):
  a, b = list(map(int, f.split("/")))
  if a % 2 == 0:
    a //= 2
  else:
    b *= 2
  return str(a) + "/" + str(b)

