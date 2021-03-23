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
  num, den = int(frac.split("/")[0]), int(frac.split("/")[1])
  if num % den == 0: return str(num // den)   
  else:
    if abs(num+0) >= den:
      if num <0:
        whole, num = abs(num) // den, abs(num) % den
        whole *= -1
      else:
        whole, num = num // den, num % den
    else:
      whole = 0
    while True:
      divided = False
      for i in [2,3,5,7,9,11,13,17,19]:
        if num % i == 0 and den % i == 0:
          num, den = num // i, den // i
          divided = True
          break
      if not divided:
        break       
  if whole == 0:
    return "{}/{}".format(num, den)
  return "{} {}/{}".format(whole, num, den)

