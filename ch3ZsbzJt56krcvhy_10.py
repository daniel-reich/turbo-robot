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

#Up to 82 digits, for more just increment "m" ...
def mid(l, h, half, sq, n):
    return [half, h] if sq < n else [l, half]
​
def square_root(n):
    m = '31622776601683793319988935444327185337195'; d = len(str(n))
    [l, h] = [int(m[:d//2])+1, (10**(d//2))**2] if d % 2 == 0 else [10**((d-1)//2), int(m[:(d+1)//2])+1]
    while d:
        half = (l+h)//2; sq = half**2
        if sq == n: return half
        l, h = mid(l, h, half, sq, n)

