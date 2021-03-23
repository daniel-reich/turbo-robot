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

from collections import deque
def parse(tokens):
    token=tokens.popleft()
    if token=='+':
            return parse(tokens)+parse(tokens)
    elif token=='-':
            return parse(tokens)-parse(tokens)
    elif token=='*':
            return parse(tokens)*parse(tokens)
    elif token=='/':
            return parse(tokens)/parse(tokens)
    else:
            return int(token)
def prefix(expr):
    return parse(deque(expr.split()))

