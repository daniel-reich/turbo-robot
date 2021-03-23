"""


Write a function that takes a string of source code and checks whether the
braces/parentheses are balanced. Every `(` or `{` must be closed by a `}` or
`)` in the opposite order. Return the index at which an imbalance occurs, or
`-1` if the string is balanced. If any `(` or `{` are never closed, return the
string's length.

### Examples

    check_balance("if (a(4) > 9) { foo(a(2)); }") ➞ -1
    # Returns -1 because it's balanced.
    
    check_balance("for (i=0;i<a(3};i++) { foo{); )") ➞ 14
    # Returns 14 because } is out of order.
    
    check_balance("if (x) {")  ➞ 8
    # Returns 8 because { is never closed.

### Notes

Think about how you can leverage [Stack Data
Structure](https://www.geeksforgeeks.org/stack-in-python/).

"""

import re
def check_balance(expression):
  pairs = {"{":"}","(":")","[":"]"}
  closed = False
  left = []
  current = None
  for i, char in enumerate(expression):
    if char in pairs.keys():
      if current:
        left.append(current)
      current = char
    elif char in pairs.values():
      if not current:
        return i
      elif pairs[current] == char:
        if left:
          current = left[-1]
          left.pop()
        else:
          current = None    
      else:
        return i
  return len(expression) if current else -1

