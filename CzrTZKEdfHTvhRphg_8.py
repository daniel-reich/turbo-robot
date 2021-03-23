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
    frac = [int(i) for i in list(frac.split('/'))]
​
    if frac[0] < 0:
        return '-{}'.format(mixed_number('{}/{}'.format(frac[0]*-1, frac[1])))
​
    whole_number = frac[0] // frac[1]
    remainder = frac[0] % frac[1]
    denominator = frac[1]
​
    if remainder == 0:
        return '{}'.format(whole_number)
    for i in range(min(frac[0], frac[1]), 1, -1):
        if remainder % i == 0 and denominator % i == 0:
            denominator //= i
            remainder //= i
            break
    if whole_number == 0:
        return str(remainder) + '/' + str(denominator)
    else:
        return str(whole_number) + ' ' + str(remainder) + '/' + str(denominator)

