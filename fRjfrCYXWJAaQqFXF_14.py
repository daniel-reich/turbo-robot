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

def isPrime(val):
  if val >= 2:
    for y in range(2, val):
      if not ( val % y ):
        return False
  else:
    return False
  return True
​
def primorial(n):
  num = 2
  primes = []
  while len(primes) < n:
    if isPrime(num):
      primes.append(num)
    num += 1
  product = 1
  for prime in primes:
    product *= prime
  return product

