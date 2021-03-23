"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

import re
from fractions import Fraction
def fractions(decimal):
  digits = re.findall(r'\d+',decimal)
  left = int(digits[0])
  if len(digits) == 2:
    x = 1
    y = pow(10,len(digits[1]))
    left = int(digits[0])
    right = int(digits[0] + digits[1])
  else:
    x = pow(10,len(digits[1]))
    y = pow(10,len(digits[1])+len(digits[2]))
    left = int(digits[0] + digits[1])
    right = int(digits[0] + digits[1] + digits[2])
​
  num = right - left
  den = y - x
  return str(Fraction(num,den))

