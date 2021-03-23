"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

def gcd(x,y):
  x,y=abs(x),abs(y)
  if x*y==0:
    return x+y
  while y!=0:
    x,y=y,x%y
  return x
def farey(n):
  fl=[(a,b) for b in range(1,n+1) for a in range(0,b+1)]
  flm=list(map(lambda x: (x[0]//gcd(*x),x[1]//gcd(*x)),fl))
  flms=list(sorted(set(flm), key=lambda x: x[0]/x[1]))
  return list(map(lambda x: str(x[0])+'/'+str(x[1]), flms))

