"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

import functools 
def isprime(n):
  for i in range(2, n//2+1):
    if n % i == 0: return False
​
  return True
​
def mult(ls):
  return functools.reduce(lambda a, b: a * b, ls)
  
def primorial(n):
  ls = []
  num = 2
  
  while len(ls) < n:
    if isprime(num):
      ls.append(num)
    num += 1
  
  return mult(ls)

