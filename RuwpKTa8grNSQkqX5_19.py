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

def fractions(decimal):
  import re
  s = float(re.sub(r'(\(|\))','',decimal))
  q = int(re.sub(r'(\(|\)|\.)','',decimal))
  y = len(re.findall(r'\.[\d]*\(', decimal)[0])-2
  x = (len(re.findall(r'[\(][\d]+[\)]', decimal)[0]) - 2) + y
  c = b = int(10 ** x - 10 ** y, )
  d = a = int(q - int(s * 10 ** y),)
  while c:
      d, c = c, d % c
  return '{}/{}'.format(int(a // d,), int(b // d,)) if d != 1 else '{}/{}'.format(a, b)

