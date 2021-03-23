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
  [a,b]=list(map(int,f.split("/")))
  def moq(a,b):
    return a  if b==0 else moq(b,a%b)
  
  return "{}/{}".format(a//moq(a,b),b//moq(a,b))

