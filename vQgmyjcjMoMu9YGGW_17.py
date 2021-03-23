"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

def simplify(txt):
  n,d = int(txt.split("/")[0]),int(txt.split("/")[1])
  g = gcd(n,d)
  if gcd==1:  return txt
  else:
    n /= g
    d /= g
  return str(int(n))+"/"+str(int(d)) if int(d)!=1 else str(int(n))
  
def gcd(a,b):
  if(b==0): return a
  else: return gcd(b,a%b)

