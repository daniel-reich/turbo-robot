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
def evaluate_polynomial(poly, num):            
    def eval_expr(string):
        regex_map = [(r'^([0-9]*[.])?[0-9]+$', lambda x: x.group(0)),
                 (r'\([^()]+\)', lambda x: eval_expr(x.group(0)[1:-1])),
                 (r'(.+)\+(.+)', lambda x: str(float(eval_expr(x.group(1))) +float(eval_expr(x.group(2))))),
                 (r'(.+)\-(.+)', lambda x: str(float(eval_expr(x.group(1))) -float(eval_expr(x.group(2))))),
                 (r'(.+)\*(.+)', lambda x: str(float(eval_expr(x.group(1))) *float(eval_expr(x.group(2))))),
                 (r'(.+)\/(.+)', lambda x: str(float(eval_expr(x.group(1))) /float(eval_expr(x.group(2))))),
                 (r'(.+)\^(.+)', lambda x: str(float(eval_expr(x.group(1)))**float(eval_expr(x.group(2)))))]
        for op, fun in regex_map:
            string = re.sub(op, fun, string)
        return string
    poly = re.sub(r'(\d|x)([x(])', r'\1*\2' ,poly) #explicit products
    poly = poly.replace('x', str(num))
    try: return float(eval_expr(poly))
    except: return 'invalid'

