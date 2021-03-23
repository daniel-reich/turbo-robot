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

import re
def prefix(exp):
  def evaluate(match):
    a,b,c,d,e = match.group(1,2,3,4,5)
    if a == "*":
      return str(int(c) * int(e))
    elif a == "+":
      return str(int(c) + int(e))
    elif a == "-":
      return str(int(c) - int(e))
    else:
      return str(int(c) // int(e))
    
  while True:
    try:
      return int(exp)
    except ValueError:
      exp = re.sub(r'([\+\-\*\/])(\s)(\-?\d+)(\s)(\-?\d+)',evaluate,exp)

