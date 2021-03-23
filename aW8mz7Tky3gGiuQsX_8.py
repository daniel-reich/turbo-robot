"""


Given a positive number x:

    p = (p1, p2, …)
    # Set of *prime* factors of x

If the square of every item in p is also a factor of x, then x is said to be a
**_powerful_** number.

Create a function that takes a number and returns `True` if it's powerful,
`False` if it's not.

### Examples

    is_powerful(36) ➞ True
    # p = (2, 3) (prime factors of 36)
    # 2^2 = 4 (factor of 36)
    # 3^2 = 9 (factor of 36)
    
    is_powerful(27) ➞ True
    
    is_powerful(674) ➞ False

### Notes

N/A

"""

def prime_factorization(n):
  i = 2
  out = []
  while i <= n:
    if n % i == 0:
      out.append(i)
      n /= i
    else:
      if i == 2:
        i = 3
      else:
        i += 2
  return out
​
​
def is_powerful(n):
  primes = set(prime_factorization(n))
  return all(n%i**2 == 0 for i in primes)

