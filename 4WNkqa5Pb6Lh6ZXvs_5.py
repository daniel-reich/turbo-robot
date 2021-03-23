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

def evaluate_polynomial(poly, x):
  valid = '1234567890+-^x()/'
  operators = '+-*/'
  if any([i not in valid for i in poly]) or '//' in poly or poly == '':
      return 'invalid'
  poly = poly.replace('^','**').replace('(','*(').replace('/','//')
  poly = list(poly)
  for i in range(len(poly)):
    if poly[i] == 'x':
      if i >= 1 and poly[i-1] not in operators and poly[i-1] != '(':
        poly[i] = '*x'
      elif i < len(poly)-1 and poly[i+1] == '(':
        poly[i] = 'x*'
  poly = ''.join(poly)
  return eval(poly)

