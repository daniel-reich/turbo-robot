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

from functools import reduce
def primorial(n):
  p = []; i=2
  while len(p) < n:
    if all(i%j for j in range(2,i)):
      p.append(i)
    i += 1
  return reduce(lambda x, y: x*y, p)

