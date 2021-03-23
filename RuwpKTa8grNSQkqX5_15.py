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
​
def fractions(decimal):
  regex_match = re.match("(\d*)\.(\d*)\((\d*)\)", decimal)
  groups = regex_match.groups()
  denom = 1
  tail = (groups[2]*10)[:15]
  original = float(groups[0] + '.' + groups[1] + tail)
  num = original
  while abs(round(num) - num) > 0.000001:
    num += original
    denom += 1
  return str(int(round(num))) + '/' + str(denom)

