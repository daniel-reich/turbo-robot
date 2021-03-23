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

def get_primes(ub):
  primes = [2]
  for c in range(3, ub + 1):
    if all(c % p != 0 for p in primes):
      primes.append(c)
  return primes
​
def power_count(n, f):
  c = 0
  while n % f == 0:
    c += 1
    n /= f
  return c
​
def express_factors(n):
  primes = get_primes(n)
  powers = [power_count(n, p) for p in primes]
  return ' x '.join('{}^{}'.format(p, f) if f > 1 else str(p) for p, f in zip(primes, powers) if f > 0)

