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
  separate=frac.split("/")
  factors=[no for no in range(1,int(separate[1])+1) if int(separate[0])%no==0 and int(separate[1])%no==0]
  if int(separate[0])==0:
    return "0"
  elif abs(int(separate[0]))<int(separate[1]):
    return str(int(separate[0])//max(factors)) +"/" +str(int(separate[1])//max(factors))
  else:
    wholeno=int(int(separate[0])/int(separate[1]))
    if wholeno*int(separate[1])==int(separate[0]):
      return str(wholeno)
    return str(wholeno) + " " +str((abs(int(separate[0]))-abs(wholeno)*int(separate[1]))//max(factors)) +"/" +str(int(separate[1])//max(factors))

