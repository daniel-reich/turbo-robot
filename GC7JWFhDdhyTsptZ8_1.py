"""


Sexy primes are primes that differ by 6.

For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a
set of sexy prime triplets.

Create a function that takes two numbers as argument, the set length `n` (2
for pairs, 3 for triplets), and the `limit`. Return a list of sorted tuples of
sexy primes up to (but excluding) the `limit`.

### Examples

    sexy_primes(2, 100) ➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]
    
    sexy_primes(3, 100) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]
    
    sexy_primes(3, 250) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]

### Notes

N/A

"""

def sexy_primes(n, limit):
  primes = [x for x in range(limit) if isPrime(x)]
  if n == 2:
    return sexyDoubles(primes)
  elif n == 3:
    return sexyTriples(primes)
​
​
​
​
def isPrime(n):
  return len([i for i in range(1,n+1) if n%i==0])==2
​
def sexyDoubles(lst):
  res = []
  for i in lst:
    for j in lst:
      if j - i == 6 and (i, j) not in res:
        res += [(i,j)]
  return res
def sexyTriples(lst):
  res = []
  for i in lst:
    for j in lst:
      for k in lst:
        if k - j == 6 and j - i == 6 and (i, j, k) not in res:
          res += [(i, j, k)]
  return res

