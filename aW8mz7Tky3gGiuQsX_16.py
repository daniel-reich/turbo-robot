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
  factors = [i for i in range(1, (n//2)+1) if is_prime(i) and not n%i]
  return all(not n%(i**2) for i in factors)
​
def is_prime(n):
  if n<2: return False
  elif n<4: return True
  return not [i for i in range(2,n) if not n%i]

