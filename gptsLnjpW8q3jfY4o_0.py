"""


Create a function that takes a integer number `n` and returns the formula for
`(a+b)^n` as a string.

### Examples

    Formula(0) ➞ "1"
    
    Formula(1) ➞ "a+b"
    
    Formula(2) ➞ "a^2+2ab+b^2"
    
    Formula(-2) ➞ "1/(a^2+2ab+b^2)"
    
    Formula(3) ➞ "a^3+3a^2b+3ab^2+b^3"
    
    Formula(5) ➞ "a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5"

### Notes

Don't put the following in your string:

  * `spaces`
  * `*`
  * `^1`
  * `a^0`
  * `b^0`

"""

from math import factorial
def Formula(n):
  def term(char,number):
    return "" if number == 0 else char if number == 1 else char + "^" + str(number)
  class Binomial:
    def __init__(self,k):
      self.c = factorial(abs(n)) // (factorial(abs(n)-k) * factorial(k))
      self.k = k
    def coefficient(self):
      return "" if self.c <= 1 else str(self.c)
    def string(self):
      return str(self.coefficient()) + term("a",abs(n)-self.k) + term("b",self.k)
    def plus(self):
      return "" if self.c == 0 or self.k == abs(n) else "+"
  terms = [Binomial(i) for i in range(0,abs(n)+1)]
  s = ''.join(list(map(lambda x: x.string() + x.plus(),terms)))
  return "1" if n == 0 else s if n > 0 else "1/({})".format(s)

