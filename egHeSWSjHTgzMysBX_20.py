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
  num, div = fract.split('/')
  num, div = int(num), int(div)
  if num % 2 == 0:
    num = num//2
  else:
    div = div*2
  return "{}/{}".format(num, div)

