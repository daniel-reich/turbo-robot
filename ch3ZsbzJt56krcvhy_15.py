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

import decimal
def square_root(big_num):
    decimal.getcontext().prec=50
    num = decimal.Decimal(big_num)
    g = decimal.Decimal(guess(num))
    for x in range(10):
        sq_rt = decimal.Decimal(g - (g**2 - num)/(2*g))
        g = sq_rt
    return int(sq_rt)
​
def guess(num):
    g_size = len(str(num))//2
    return int('1' + '0'*g_size)

