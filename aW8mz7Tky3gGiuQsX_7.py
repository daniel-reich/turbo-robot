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
  def is_prime(num):
    flag = True
    for i in range(2, num-1):
      if num%i==0:
        flag = False
    return flag
  factors = []
  prime_factors = []
  for i in range(2,n-1):
    if n%i == 0:
      factors.append(i)
      if is_prime(i):
        prime_factors.append(i)
  squares = []
  for f in prime_factors:
    squares.append(f**2)
  flag = True
  for f in squares:
    if f not in factors:
      flag = False
  return flag

