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
  i1 = int(fract[fract.find("/")+1:])
  i2 = int(fract[:fract.find("/")])
  if i2%2 == 0:
   return "{}/{}".format(int(i2/2),int(i1))
  if i2%2 != 0:
   return "{}/{}".format(int(i2),int(i1*2))

