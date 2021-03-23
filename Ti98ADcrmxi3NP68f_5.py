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

def greaterThanOne(frac):
  x = frac.split('/')
  if int(x[0])/int(x[1]) > 1:
    return True
  else: 
    return False

