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
  c = [int(i) for i in fract]
  return '{}/{}'.format(round(c[0] /2 if c[0]%2 == 0 else c[0]) , round(c[1]* 2 if c[0] % 2 ==1 else c[1]))

