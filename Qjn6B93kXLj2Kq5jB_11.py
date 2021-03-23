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
  f=[int(i) for i in f.split('/')]
  a=f[0]
  b=f[1]
  for i in range(2,f[0]+1):
    if f[0]%i==0 and f[1]%i==0: 
      a=f[0]/i
      b=f[1]/i
  return str(int(a))+'/'+str(int(b))

