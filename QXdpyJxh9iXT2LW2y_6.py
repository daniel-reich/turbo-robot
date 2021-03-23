"""


In mathematics, a semiprime is a natural number that is the product of two
prime numbers. The two primes in the product may equal each other, so the
semiprimes include the squares of prime numbers.

Create a function that takes a number `n` as an argument and returns two
lists, one list with all the semiprimes < `n` and the other with all the
semiprimes < `n` and that are not square numbers.

### Examples

    semiprimes(20) ➞ ([4, 6, 9, 10, 14, 15], [6, 10, 14, 15])
    
    semiprimes(157) ➞ ([4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 121, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155], [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155])
    
    semiprimes(1), ([], [])

### Notes

N/A

"""

import math
def check(n):
  if n == 1: 
    return False
  if n == 2: 
    return True
  pri = True
  for i in range(2, n): 
    if n%i == 0: 
      pri = False
  return pri
​
def product_of_primes(num):
  if check(num): 
    return False
  l = []
  for i in range(2, num): 
    if num%i == 0:
      l.append(i)
  if all(check(i)for i in l): 
    return True
  else: 
    return False
def square(h): 
  if round(math.sqrt(h))**2 == h: 
    return True
  else: 
    return False
def semiprimes(n):
  l = []
  for i in range(2, n): 
    if product_of_primes(i): 
      l.append(i)
  ll = []
  for i in l: 
    if not square(i): 
      ll.append(i)
  return (l, ll)

