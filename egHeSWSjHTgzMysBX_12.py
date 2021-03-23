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
  f = fract.split("/")
  if int(f[0]) % 2 == 0:
    return str(int(f[0]) // 2) + "/" + f[1]
  else:
    return f[0] + "/" + str(int(f[1]) * 2)

