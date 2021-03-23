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

def check_balance(expression):
  A=[]
  for i, x in enumerate(expression):
    if x=='(':
      A.append((1,i))
    elif x==')':
      A.append((-1,i))
    elif x=='{':
      A.append((2,i))
    elif x=='}':
      A.append((-2,i))
    else:
      A.append((0,i))
  B=[x for x in A if x[0]!=0]
  stack=[]
  for x in B:
    if x[0]==1 or x[0]==2:
      stack.append(x)
    else:
      if len(stack)>0 and x[0]+stack[-1][0]==0:
        stack.pop()
      else:
        return x[1]
        break
  if len(stack)==0:
    return -1
  else:
    return stack[0][1]+1

