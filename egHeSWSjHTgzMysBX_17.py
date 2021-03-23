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
  x,y=[int(i) for i in fract.split('/')]
  return str(x//2)+'/'+str(y) if x%2==0 else str(x)+'/'+str(y*2)

