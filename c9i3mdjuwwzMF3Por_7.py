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

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if not n % k:
            return False
    return True
​
​
def is_flippable(n):
    return all(c in '01689' for c in str(n))
​
​
def flip_num(n):
    return int(''.join({'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}[c]
                       for c in str(n)))
​
​
def bemirp(n):
    if str(n) != str(n)[::-1] and is_prime(n) and is_prime(int(str(n)[::-1])):
        if is_flippable(n):
            flipped_n = flip_num(n)
            if is_prime(flipped_n) and is_prime(int(str(flipped_n)[::-1])):
                return 'B'
        return 'E'
    elif is_prime(n):
        return 'P'
    else:
        return 'C'

