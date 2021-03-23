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

def factors(n):
  output = []
  for i in range(1, n+1):
    if n % i == 0:
      output.append(i)
  return output
​
def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  return True
​
def is_powerful(n):
  prime_factors = [i for i in factors(n) if is_prime(i)]
  for i in prime_factors:
    if i**2 not in factors(n):
      return False
  return True

