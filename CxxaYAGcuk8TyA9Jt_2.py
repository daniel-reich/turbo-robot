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

brackets = {')': '(', '}': '{'}
​
def checkBalance(expression):
    stack = []
    for i in range(len(expression)):
        c = expression[i]
        if c in brackets:
            if len(stack) == 0 or stack[-1] != brackets[c]:
                return i
            stack.pop()
        elif c in brackets.values():
            stack.append(c)
    return -1 if len(stack) == 0 else len(expression)

