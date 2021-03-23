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

def check(n):
  if n == 1: 
    return False
  if n == 2:
    return True
  prime = True
  for i in range(2, n): 
    if n%i == 0:
      prime = False
  return prime
def primorial(n):
  l = []
  for i in range(1, 50): 
    if check(i): 
      l.append(i)
  count = 1
  for i in range(n): 
    count *= l[i]
  return count

