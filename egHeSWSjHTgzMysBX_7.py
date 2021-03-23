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
  fr = list(map(int,fract.split("/")))
  if int(fr[0]) % 2 == 0:
    return str(fr[0]//2)+"/"+str(fr[1])
  else:
    return str(fr[0])+"/"+str(fr[1]*2)

