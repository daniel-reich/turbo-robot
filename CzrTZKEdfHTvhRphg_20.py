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

def pgcd(num1, num2):
    for val in range(min(num1, num2), 0, -1):
        if num2%val == 0 and num1%val == 0 : return val
​
def mixed_number(frac):
    up, down = list(map(lambda elm: int(elm), frac.split('/')))
    if up == 0: return '0'
    up = abs(up)
    div = pgcd(up, down)
    up, down = up//div, down//div
    
    num = up//down
    result = '-' if frac[0] == '-' else ''
    if num == up/down: return result + str(num)
    result += str(num)+' ' if num != 0 else ''
    result += str(up - num*down) + '/' + str(down) if num != up/down else str(num)
    
    return result

