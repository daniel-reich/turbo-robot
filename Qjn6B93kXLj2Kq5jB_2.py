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

def gcd(a,b):
  return b if a == 0 else gcd(b%a,a)
​
def simplify_frac(f):
  a,b = (int(e) for e in f.split('/'))
  g = gcd(a,b)
  return str(a//g) + '/' + str(b//g)

