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
  fs = f.split('/')
  num = int(fs[0])
  den = int(fs[1])
  for i in reversed(range(num+1)):
    if num%i==0 and den%i==0:
      return str(num//i)+'/'+str(den//i)

