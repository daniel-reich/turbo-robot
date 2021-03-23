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

from numpy import prod
​
def primorial(n):
  lst = [2]
  x = 3
  while len(lst) < n:
    for i in lst:
      if not x % i:
        x+=2
        continue
    lst.append(x)
    x += 2
  return prod(lst)
