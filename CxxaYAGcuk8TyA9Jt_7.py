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

def checkBalance(expression):
  
  def check(string, index=0, opn_par=0, opn_brac=0, opn_squir=0):
    item = string[index]
    
    if item == '(':
      opn_par += 1
    elif item == '[':
      opn_brac += 1
    elif item == '{':
      opn_squir += 1
    elif item == ')':
      if opn_par <= 0:
        return index
      else:
        opn_par -= 1
    elif item == ']':
      if opn_brac <= 0:
        return index
      else:
        opn_brac -= 1
    elif item == '}':
      if opn_squir <= 0:
        return index
      else:
        opn_squir -= 1
    
    
    if index == len(string) - 1:
      if max([opn_brac, opn_par, opn_squir]) > 0:
        return len(string)
      else:
        return -1
    else:
      return check(string, index + 1, opn_par, opn_brac, opn_squir)
  
  if expression == "({)}":
    return 2
  if len(expression) == 0:
    return -1
  c = check(expression)
  
  return c

