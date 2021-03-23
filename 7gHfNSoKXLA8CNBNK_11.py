"""


Create a function that takes a number `max_den` and returns the total number
of fully simplified proper fractions that exist with denominator less than or
equal to `max_den`.

You only need to return the number of fractions; **NOT the fractions
themselves**. In the examples below, I list the fractions simply for your
reference.

### Examples

    sim_prop_frac(10) ➞ 31
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1/8, 3/8, 5/8, 7/8, 1/9, 2/9, 4/9, 5/9, 7/9, 8/9, 1/10, 3/10, 7/10, 9/10
    
    sim_prop_frac(7) ➞ 17
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7

### Notes

A fully simplified proper fraction is a fraction where both the numerator and
denominator share no common factors besides 1 and the fraction is less than 1.

"""

def sim_prop_frac(max_den):
​
  class Fraction:
​
    def __init__(self, numerator, denominator):
      self.n = numerator
      self.d = denominator
    
    def simplify(self):
      def GCD(n1, n2):
​
        n1factors = []
        n2factors = []
​
        for n in range(1, min([n1, n2]) + 1):
​
          if n1 % n == 0:
            n1factors.append(n)
          if n2 % n == 0:
            n2factors.append(n)
        
        for factor in reversed(n1factors):
          if factor in n2factors:
            return factor
      
      gcd = GCD(self.n, self.d)
    
      self.n /= gcd
      self.d /= gcd
​
      return '{}/{}'.format(self.n, self.d)
  
  fractions = []
​
  for n in range(2, max_den + 1):
    for num in range(1, n):
      frac = Fraction(num, n)
      fractions.append(frac)
  
  simplified = set()
​
  for frac in fractions:
    simplified.add(frac.simplify())
  
  return len(list(simplified))

