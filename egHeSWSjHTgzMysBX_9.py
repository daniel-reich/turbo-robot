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
  fract_list = fract.split('/')
  if int(fract_list[0])%2==0:
    fract_list[0] = str(int(fract_list[0])//2)
  else:
    fract_list[1] = str(int(fract_list[1])*2)
  return '/'.join(fract_list)

