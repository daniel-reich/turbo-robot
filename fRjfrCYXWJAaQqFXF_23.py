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

def prime_list(n):
  x = 1
  l = []
  while len(l) < n:
    k = []
    for i in range(1,x+1):
      if x%i==0:
        k.append(i)
    if len(k) == 2:
      l.append(x)
    x +=1
  return l
def primorial(n):
  product = 1
  for i in prime_list(n):
    product *= i
  return product

