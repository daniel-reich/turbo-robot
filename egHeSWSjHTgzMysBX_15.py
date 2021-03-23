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
  fract = fract.split('/')
  if int(fract[0]) % 2 == 1:
     return(fract[0] + '/' + str(2 * int(fract[1])))
  else:
     return(str(int(fract[0])//2) + '/' + fract[1])

