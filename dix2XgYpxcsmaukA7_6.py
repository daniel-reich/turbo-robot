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

from collections import Counter
​
def express_factors(num):
  factors = factorization(num)
  print (factors)
  cnt = Counter(factors)
  pairs = sorted([[k,v] for k,v in cnt.items()], key= lambda x: x[0])
  print(pairs)
  res = []
  for pair in pairs:
    k,v = pair
    if v > 1:
      res.append(str(k) + "^" + str(v))
    else:
      res.append(str(k))
  return " x ".join(res)
​
def primes (num):
    primes = [2]
    number = 3
    while number <= num :
        if not any([number % p == 0 for p in primes]):
            primes.append(number)
        number += 2
    return primes
​
def factorization(num):
    prim = primes(num)
    factors = []
    for p in prim:
        while num % p == 0:
            factors.append(p)
            num = num // p
    return factors

