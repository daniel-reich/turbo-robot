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

def primes(n):
  res = []
  while n > 1:
    for x in range(2, n + 1):
      if n % x == 0:
        n = int(n/x)
        res.append(x)
        break
  return res
​
def is_powerful(n):
  ps = primes(n)
  return all(ps.count(p) > 1 for p in ps)

