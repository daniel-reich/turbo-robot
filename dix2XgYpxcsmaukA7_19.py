"""


Create a function that takes a positive integer and returns a string
expressing how the number can be made by multiplying powers of its prime
factors.

### Examples

    express_factors(2) ➞ "2"
    
    express_factors(4) ➞ "2^2"
    
    express_factors(10) ➞ "2 x 5"
    
    express_factors(60) ➞ "2^2 x 3 x 5"

### Notes

  * All inputs will be positive integers in the range 1 < n < 10,000.
  * If a factor is repeated express it in the form **"x^y"** where x is the factor and y is the number of repetitions of the factor.
  * If `n` is a prime number, return `n` as a string as in example #1 above.
  * Factors should appear in ascending order in the expression.
  * Make sure you include the space either side of the multiplication sign, `" x "`.
  * Check the **Resources** if you need to understand **Prime Factorization**.

"""

def express_factors(n):
  factors = list(filter(lambda x: n % x == 0,range(2,n+1)))
  factor = factors[0]
  if len(factors) == 1:
    return str(n)
  if n % pow(factor,2) > 0:
    return str(factor) + ' x ' + express_factors(n//factor)
  exponent = 0
  while n % factor == 0 and n > factor:
    exponent += 1
    n = n//factor
  if n == factor:
    return str(n) + '^'+ str(exponent+1)
  return str(factor) + '^' + str(exponent) + ' x ' + express_factors(n)

