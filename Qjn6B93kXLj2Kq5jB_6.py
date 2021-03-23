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
  def GCD(n1, n2):
    def factors(n):
      facts = []
      for num in range(1, n + 1):
        if n%num == 0:
          facts.append(num)
      return facts
    
    n1factors = factors(n1)
    n2factors = factors(n2)
    
    common_denominators = []
  
    for factor in n1factors:
      if factor in n2factors:
        common_denominators.append(factor)
    
    return max(common_denominators)
  
  frac = f.split('/')
  
  numerator = int(frac[0])
  denominator = int(frac[1])
  
  gcd = GCD(numerator, denominator)
  
  numerator /= gcd
  denominator /= gcd
  
  return '{}/{}'.format(int(numerator), int(denominator))

