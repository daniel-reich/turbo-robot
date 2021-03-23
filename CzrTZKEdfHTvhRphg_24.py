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
  if frac.split('/')[0] == '0':
    return '0'
  num, den = [int(i) for i in frac.split('/')]
  string = ''
  if abs(num) > den:
    string += str(abs(num) // den)
  num = abs(num) % den
  num, den = num // (gcd(num,den)), den // (gcd(num,den))
  if abs(num) > 0:
    if len(string) > 0:
      string += ' '
    string += str(num) + '/' + str(den)
  if '-' in frac:
    string = '-' + string
  return string
    
def gcd(x,y):
  while(y):
    x,y = y, x%y
  return x

