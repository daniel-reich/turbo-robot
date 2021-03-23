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
  divisors = [a for a in range(1, n) if n % a == 0]
  pdiv = [a for a in divisors if len([i for i in range(1, a+1) if a % i == 0]) == 2]
  count = 0
  for i in pdiv:
    if i**2 not in divisors:
      count += 1
  return count == 0

