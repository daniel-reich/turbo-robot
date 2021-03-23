"""


You will be given a polynomial expression in string form. The expression will
contain any of the following operations, written using standard mathematical
notation for a single variable, "x", as illustrated in the examples below:

  * addition: x + 1
  * subtraction: x – 2
  * multiplication: 3x
  * division: x / 4
  * exponentation: x^5
  * brackets: x(x + 1)

Your task is to write a function that can evaluate such a polynomial for a
given value of x. You will receive two arguments: the polynomial string and
the input number.

If the mathematical expression contains an error, you should return
`"invalid"`.

### Examples

    evaluate_polynomial("x+1", 5) ➞ 6
    
    evaluate_polynomial("5x^2", 3) ➞ 45
    
    evaluate_polynomial("(x(x+1))/2", 4) ➞ 10
    
    evaluate_polynomial("4(x + 3))/2", 5) ➞ "invalid"
    # Invalid because parentheses not balanced.

### Notes

The string will not contain spaces.

"""

import re
​
def evaluate_polynomial(poly, num):
  if '&' in poly or '//' in poly: return 'invalid'
  poly = poly.replace('x', str(num))
  if '^' in poly:
    s = poly.split('^')
    if len(s[0]) == 2:
      s[0] = s[0][:1] + '*' + s[0][1]
    poly = '**'.join(s)
  elif '(' in poly:
    poly = poly.replace('(', '*(')
  
  try: 
    return eval(poly)
  except:
    return 'invalid'
  
  #poly = poly.replace('(', '*(').replace('x', str(num))
  #print(poly, eval(poly))
  #t = re.sub('[0-9]+[x]', '[0-9]+[*][x|(]', poly)

