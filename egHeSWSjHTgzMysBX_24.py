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
  f = f.split('/')
  f[0] = int(f[0])
  f[1] = int(f[1])
  if f[0] % 2 == 1:
    f[1] = f[1] * 2
  else:
    f[0] = f[0] / 2
  f[0] = str(int(f[0]))
  f[1] = str(int(f[1]))
  return '/'.join(f)

