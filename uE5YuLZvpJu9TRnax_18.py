"""


Create a function that takes a mathematical expression in **prefix notation**
as a string and evaluates the expression.

### Examples

    prefix("+ 5 4") ➞  9
    
    prefix("* 12 2") ➞  24
    
    prefix("+ -10 10") ➞  0

### Notes

  * The mathematical expression is valid.
  * Check the **Resources**.
  * Use `//` for division.

"""

def calculator(a, op, b):
  return {
    '+': a + b,
    '-': a - b,
    '//': a / b,
    '*': a * b,
  }[op]
​
import re
​
def prefix(exp):
  lst =  exp.replace('/', '//').split(' ')[::-1]
  res = []
  for i in lst:
    if bool(re.match(r'^-?\d+$', i)):
      res.append(i)
    else:
      res.append(calculator(int(res.pop()), i, int(res.pop())))
  return res[0]

