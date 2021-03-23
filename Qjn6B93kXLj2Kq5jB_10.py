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
  a,b=f.split('/')
  r=[i for i in range(1,int(a)+1) if int(a)%i==0]
  g=[j for j in range(1,int(b)+1) if int(b)%j==0]
  v=max(list(set(r).intersection(set(g))))
  x=int(a)//v
  y=int(b)//v
  return str(x)+'/'+str(y)

