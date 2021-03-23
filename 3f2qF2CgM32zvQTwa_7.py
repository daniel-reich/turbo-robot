"""


Given a simple _math expression_ as a string, neatly format it _as an
equation_.

### Examples

    format_math("3 + 4") ➞ "3 + 4 = 7"
    
    format_math("3 - 2") ➞ "3 - 2 = 1"
    
    format_math("4 x 5") ➞ "4 x 5 = 20"
    
    format_math("6 / 3") ➞ "6 / 3 = 2"

### Notes

  * You will need to deal with **addition** , **subtraction** , **multiplication** and **division**.
  * Division will have **whole number** answers (and will obviously **not** involve 0).

"""

def format_math(expr):
  new = ''
  if 'x' in expr:
    new = expr.replace('x','*')
  else:
    new = expr
    
  answer = int(eval(new))
  
  return "{} = {}".format(expr, answer)

