"""


A prime number is a number whose only proper (non-self) divisor is 1 (example
13).

An emirp (prime spelled backwards) is a non-palindromic prime which, when its
digits are reversed, makes _another_ prime. E.g. 13 is a prime, and so is 31.
Both are therefore emirps.

A bemirp is a prime which is an emirp (makes another prime with its digits
reversed), but additionally, makes another prime when flipped upside down (see
note). The upside-down version is also an emirp, which makes a group of 4
primes. Bemirps consist only of digits 0, 1, 6, 8, and 9.

To illustrate: 11061811, reversed = 11816011, upside-down = 11091811, upside-
down reversed = 11819011. All four are primes.

Create a function that takes a number and returns `"B"` if it’s a bemirp,
`"E"` if it's a (non-bemirp) emirp, `"P"` if it's a (non-emirp) prime, or
`"C"` (composite / non-prime).

### Examples

    bemirp(101) ➞ "P"
    
    bemirp(1011) ➞ "C"
    
    bemirp(1069) ➞ "E"
    
    bemirp(1061) ➞ "B"

### Notes

6 upside-down is 9 and vice-versa. 0, 1, and 8 are unchanged when flipped. The
remaining five digits are unflippable.

"""

import math
​
upDown = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}
​
def isPrime(n):
    n = abs(int(n))
    if n == 2: return True
    if n % 2 == 0: return False
    r = math.sqrt(n)
    x = 3 
    while x <= r:
        if n % x == 0: return False
        x += 2
    return True     
​
def bemirp(n):
    if not isPrime(n):
        return 'C'
    emirp = int(str(n)[::-1])
    if not isPrime(emirp) or emirp == n:
        return 'P'
    bemirp = ""
    for digit in str(n):
        if digit not in upDown:
            return 'E'
        bemirp += upDown[digit]
    bemirp = int(bemirp)
    if not isPrime(bemirp):
        return 'E'
    else:
        return 'B'

