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

def reverse(n):
    return int(str(n)[::-1])
​
def up_down(n):
    s = ''
    for i in str(n):
        s += '6' if i == '9' else '9' if i == '6' else i
    return int(s)
​
def isprime(n):
    return all( n % i for i in range(2,n//2+1))
​
def bemirp(n):
    if isprime(n):
        if n != reverse(n) and isprime(reverse(n)):
            if isprime(up_down(n)) and isprime(reverse(up_down(n))):
                return 'B'
            return 'E'
        return 'P'
    return 'C'

