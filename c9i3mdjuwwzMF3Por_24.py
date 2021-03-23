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
  n = int(n)
  if n == 2 or n == 3: return True
  elif n < 2 or n%2 == 0: return False
  elif n < 9: return True
  elif n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True
​
def bemirp(n):
  n, f = str(n), ''.join(k if k in '018' else {'6':'9', '9':'6'}[k] for k in str(n)) if all(int(k) in (0, 1, 6, 8, 9) for k in str(n)) else None
  r, rf = str(n)[::-1], str(f)[::-1] if f else None
  o = 'C'
  if is_prime(n): o = 'P'
  if o == 'P' and is_prime(r) and f and f!=n: o = 'E'
  if o == 'E' and f and is_prime(f) and rf and is_prime(rf): o = 'B'
  return o
​
# The function to check if a number is prime was the hardest part :`D

