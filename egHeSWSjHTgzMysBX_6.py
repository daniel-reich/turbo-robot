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
  num = list(map(int,fract.split("/")))
  if num[0]%2 == 0:
    num[0] = int(num[0]/2)
  else:
    num[1] = num[1]*2
  return str(num[0]) + "/" +str(num[1])

