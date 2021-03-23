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
  def Prime_Factors(n):
    factors = []
    
    for num in range(2, n):
      while n%num == 0:
        factors.append(num)
        n /= num
    return list(set(factors))
  def Factors(n):
    facts = []
    
    for num in range(2, n):
      if n%num == 0:
        facts.append(num)
    
    return facts
  
  pf = Prime_Factors(n)
  fs = Factors(n)
  
  squares = []
  
  for prime in pf:
    squares.append(prime**2)
  
  for square in squares:
    if square not in fs:
      return False
  return True

