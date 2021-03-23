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
  slash = frac.find("/")
  num = int(frac[:slash])
  dem = int(frac[slash+1::])
  if num == 0:
    return "0"
  elif num % dem == 0:
    return str(num // dem)
  elif abs(num) == 1:
    return frac
  else:
    n = abs(num)
    d = abs(dem)
    w = n // d
    factors = [i for i in range(1,min(n,d)) if n % i == 0 and d % i == 0]
    gcd = factors[-1]
    if gcd == 1 and n < d:
      return frac
    else:
      n = n // gcd
      d = d // gcd
      if num < 0:
        w = -1 * w
      if abs(num) < abs(dem):
        return "{}/{}".format(str(n % d), str(d))
      else:
        return "{} {}/{}".format(str(w), str (abs(n % d)), str(d))

