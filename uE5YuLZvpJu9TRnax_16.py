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

def prefix(exp):
  exp=exp.replace('/', '//')
  A=exp.split()
  stack=[]
  for x in A[::-1]:
    if x not in {'+', '-', '*', '//'}:
      stack.append(x)
    else:
      stack.append(str(eval(stack.pop()+x+stack.pop())))
  return int(stack[0])

