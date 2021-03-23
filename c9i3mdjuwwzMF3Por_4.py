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

def isprime(n):
  for i in range(n):
    if i<2:
      continue
    if n%i==0:
      return False
      break
  else:
    return True
    
def isbemirp(n):
  lst=','.join(str(n)).split(',')
  ls=[]
  for i in lst:
    if i=='6':
      ls.append('9')
    elif i=='9':
      ls.append('6')
    else:
      ls.append(i)
  num=int(''.join(ls))
  if isprime(num) and isprime(int(str(num)[::-1])):
    return True
  else:
    False
    
def bemirp(n):
  if not isprime(n):
    return 'C'
  else:
    if str(n)==str(n)[::-1]:
      return 'P'
    elif not isprime(int(str(n)[::-1])):
      return 'P'
    elif isbemirp(n):
      return 'B'
    else:
      return 'E'

