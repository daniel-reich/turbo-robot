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
  s=list(map(int,fract.split("/")))
  return "/".join(map(str,[s[0]//2 if s[0]%2==0 else s[0],s[1] if s[0]%2==0 else s[1]*2]))

