"""


Given a fraction as a string, return whether or not it is greater than 1 when
evaluated.

### Examples

    greater_than_one("1/2") ➞ False
    
    greater_than_one("7/4") ➞ True
    
    greater_than_one("10/10") ➞ False

### Notes

Fractions must be strictly **greater** than 1 (see example #3).

"""

def greater_than_one(frac):
  frac = frac.split("/")
  fract = int(frac[0])/int(frac[1])
  if (fract > 1):
    return True
  else:
    return False

