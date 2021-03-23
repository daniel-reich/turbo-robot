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

from decimal import*
def square_root(n):
  getcontext().prec=42
  x,c=Decimal(n),0 
  while 1: 
      c,r=c+1,Decimal(.5)*(x+(n/x))
      if abs(r-x)<1e-5:return r 
      x=r

