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

def checkPrime(n):
    isPrime = True
    for j in range(2,int(n**.5)+1):
        if n % j == 0:
            return False
    return True
​
def bemirp(n):
    myans = ''
    l = len(str(n))
    non = ['2','3','4','5','7']
​
    #Check Prime
    if checkPrime(n):
        myans = 'P'
    else:
        return 'C'
    #Check Emirp
    nn = int(str(n)[::-1])
    if checkPrime(nn) and n != nn:
        myans = 'E'
    #Check Bemirp
    t = str(n)
    tt = str(nn)
    for item in t:
        if item in non:
            return myans
    nt = ''
    for item in t:
        if item == '6':
            nt += '9'
        elif item == '9':
            nt += '6'
        else:
            nt += item
​
    nnt = ''
    for item in tt:
        if item == '6':
            nnt += '9'
        elif item == '9':
            nnt += '6'
        else:
            nnt += item
​
    if checkPrime(int(nt)) and checkPrime(int(nnt)) and n != nn:
        myans = 'B'
​
​
    return myans

