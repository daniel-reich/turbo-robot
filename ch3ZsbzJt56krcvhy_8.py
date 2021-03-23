"""


This is a big integer challenge. You are given an integer which is a **perfect
square**. It is composed of 40 or more digits. Compose a function which will
find the exact square root of this integer.

### Examples

    square_root(152415787532388367501905199875019052100) ➞ 12345678901234567890
    
    square_root(10203040506070809101112131413121110090807060504030201) ➞ 101010101010101010101010101

### Notes

  * All test cases are perfect squares.
  * A **good fortune** bonus awaits you if you are able to complete this challenge without importing anything.

"""

def square_root(n):
  k = len(str(n))
  x = 10**(k//2)
  for i in range(15):
    x = (x + n//x)//2
  if x**2 == n: return x
  if (x-1)**2 == n: return x-1
  if (x+1)**2 == n: return x+1

