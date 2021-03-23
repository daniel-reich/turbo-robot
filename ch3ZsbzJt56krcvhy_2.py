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

def square_root(n):                 # Big squares
  """ Return the square root of huge number """
  if n < (1<<50): return int(n**0.5)
  r = 1 << ((n.bit_length() + 1) >> 1)
  while True:
    num = (r+n//r) >> 1
    if num >= r:
      return r
    r = num

