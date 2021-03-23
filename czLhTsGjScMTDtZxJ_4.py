"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

prime = lambda num: len([n for n in range(2, num) if num % n == 0]) == 0
multipliers = lambda lst, index: lst[:index]
​
def primes(goal):
  prs = []
  n = 2
  while len(prs) < goal:
    if prime(n) == True:
      prs.append(n)
    n += 1
  return prs
​
def multiplier(multipliers):
  product = 1
  
  for multi in multipliers:
    product *= multi
  
  return product
  
primes = primes(9)
​
def primorial(n):
  
  m = multipliers(primes, n)
  return multiplier(m)

