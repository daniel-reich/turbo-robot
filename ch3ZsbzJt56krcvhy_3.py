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
  start = 1
  end = n
  if n == 0 or n == 1:
    return n
  while start <= end:
    mid = (start+end)//2
    if mid*mid == n:
      return mid
    elif mid*mid < n:
      start = mid+1
    else:
      end = mid-1

