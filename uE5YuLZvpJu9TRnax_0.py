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

def prefix(e):
  s=[]
  for x in e.split():s.append(x if x in'+-*/'or s[-1]in'+-*/'else str(eval(s.pop()+s.pop().replace('/','//')+x)))
  while len(s)>1:
    e=s
    s=[]
    for x in e:s.append(x if x in'+-*/'or s[-1]in'+-*/'else str(eval(s.pop()+s.pop().replace('/','//')+x)))
  return int(s[0])

