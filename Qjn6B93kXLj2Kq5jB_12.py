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
  new=""
  f=f.split("/")
  n=0
  for i in range(1,int(f[0])+1):
    for j in range(1,int(f[1])+1):
      if int(f[0])%i==0 and int(f[1])%j==0:
        if i==j:
          n=i
  f[0]=int(f[0])//n
  f[1]=int(f[1])//n
  new=str(f[0])+"/"+str(f[1])
  return new

