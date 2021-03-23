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
​
  f,i = [],0
  
  for i in range(2,n):
    while not n%i:
      n/=i
      f.append(i)
​
    i += 1
​
  return list(set(f))
​
def is_prime(l):
​
  for e in l:
    for i in range(2,n):
      if not e%i:
        l.pop(e)
​
  return l
​
def is_powerful(n):
  
  fs = factors(n)
  
  for i in fs:
    if n%(i**2):
      return False
​
  return True

