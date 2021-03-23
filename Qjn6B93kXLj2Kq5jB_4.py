"""


Create a function which _simplifies_ a given **fraction** into its **simplest
ratio**. Return the fraction as a _string_.

### Examples

    simplify_frac("2/4") ➞ "1/2"
    
    simplify_frac("15/25") ➞ "3/5"
    
    simplify_frac("4/9") ➞ "4/9"

### Notes

  * Fractions are given as strings.
  * Return the same fraction if it is already in its simplified ratio (see example #3).

"""

def simplify_frac(f):
  parts = f.split('/')
  den = int(parts[0])
  num = int(parts[1])
  gcd_val = gcd(den,num)
  if gcd_val == 1:
    return f
  else:
    den = int(den / gcd_val)
    num = int(num / gcd_val)
    return str(den) + "/" + str(num)
  
def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

