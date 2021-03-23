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
  exp = ['/', '+', '-', 'x']
  oper = ''
  expr = expr.strip()
  answer = 0
  for e in expr:
    if e in exp:
      oper = e
  num = expr.split(oper)
  if oper == '+':
    answer = expr + ' = ' + str(int(int(num[0]) + int(num[1])))
  elif oper == '-':
    answer = expr + ' = ' + str(int(int(num[0]) - int(num[1])))
  elif oper == 'x':
    answer = expr + ' = ' + str(int(int(num[0]) * int(num[1])))
  else:
    answer = expr + ' = ' + str(int(int(num[0]) / int(num[1])))
  return(answer)

