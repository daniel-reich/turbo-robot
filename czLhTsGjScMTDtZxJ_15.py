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

def is_prime(n):
  if n%2==0:return False
  for i in range(3,n):
    if n%i==0:return False
  return True
def primorial(n):
  ans=1
  primes=[2]
  check=3
  while True:
    if len(primes)==n:
      for i in primes:
        ans*=i
      return ans
    else:
      if is_prime(check):
        primes.append(check)
        check+=1
      else:check+=1

