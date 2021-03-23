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

def is_powerful(n):
  facs = get_factors(n)
  for fac in facs:
    if is_prime(fac) and (fac**2) not in facs:
      return False
  return True
  
  
def get_factors(n):
  res = []
  for i in range(2, n-1):
    if not n % i:
      res.append(i)
  return res
  
def is_prime(n):
  if n < 2:
      return False
  else:
      for i in range(2, int(abs(n**0.5)) + 1):
          if not n % i:
              return False
      return True

