"""


Create a function that takes a string representing a fraction, and return a
string representing that input as a mixed number.

  * Mixed numbers are of the form `1 2/3` — note the space between the whole number portion and the fraction portion.
  * Resulting fractions should be fully reduced (see example #2).
  * If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
  * If a result is only fractional with no whole number, return only the fractional portion (see example #4).
  * If a result is negative, the whole number should carry the negative sign. If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).

### Examples

    mixed_number("5/4") ➞ "1 1/4"
    
    mixed_number("6/4") ➞ "1 1/2"
    
    mixed_number("8/4") ➞ "2"
    
    mixed_number("4/6") ➞ "2/3"
    
    mixed_number("-1/4") ➞ "-1/4"
    
    mixed_number("-5/4") ➞ "-1 1/4"
    
    mixed_number("-8/4") ➞ "-2"

### Notes

All provided inputs will be formatted similarly, negative numbers will be
provided in the numerator portion only, and all inputs will contain no spaces,
invalid characters, or zero denominators.

"""

def mixed_number(frac):
  f = [int(i) for i in frac.split('/')]
  if not f[0]: return '0'
  whole = (abs(f[0])//f[1]) * f[0]//abs(f[0])
  rem = abs(f[0])%f[1]
  return reduce(f[0],f[1]) if not whole else str(whole) if not rem else "{} {}".format(whole, reduce(rem, f[1]))
  
def reduce(n1,n2):
  return '{}/{}'.format(n1//gcd(n2,n1),n2//gcd(n2,n1))
​
def gcd(a,b):
  if b==0:
    return abs(a)
  return gcd(b, a%b)

