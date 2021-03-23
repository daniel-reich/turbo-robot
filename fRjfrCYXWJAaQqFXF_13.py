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

def primorial(n):
  
  def is_prime(num):
    for i in range(2, num):
      if num%i == 0:
        return False
    return True
​
  def next_prime():
    i = 2
    while True:
      if is_prime(i):
        yield i
      i += 1
      
  primorial = 1
  p = next_prime()
​
  for i in range(n):
    primorial *= next(p)
​
  return primorial

