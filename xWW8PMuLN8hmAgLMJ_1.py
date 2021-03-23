"""


Mathematical expressions are usually written with _infix_ notation, where the
operator is _in-between_ the two operands. _Postfix_ notation, on the other
hand, is where the operator _follows_ the operands. As we use operator
precedence to determine the order of calculation (e.g. multiplication/division
is evaluated before addition/subtraction), we can change the position of the
operands and eliminate the need for parentheses:

    2 + 5   # Infix
    2 5 +   # Postfix
    
    5 + (1 + 2) * 4 - 3   # Infix
    5 1 2 + 4 * + 3 -     # Postfix

Postfix expressions are evaluated by reading left-to-right. Any time an
operator is reached, a calculation is performed on the previous two operands.
The process repeats until there are no more calculations to perform:

    2 3 4 * + 9 -   # evaluate 3x4
       2 12 + 9 -   # evaluate 2+12
           14 9 -   # evaluate 14-9
                5   # final answer

Given a postfix expression as a string, return the evaluated expression. A
single space separates each operator/operand.

### Examples

    postfix("12 3 /") ➞ 4
    
    postfix("5 3 4 * +") ➞ 17
    
    postfix("5 3 + 4 *") ➞ 32

### Notes

Postfix is also known as "Reverse Polish Notation". See the resources tab for
more information.

"""

import operator
from collections import deque
op_map = {'+' : operator.add,
          '-' : operator.sub,
          '*' : operator.mul,
          '/' : operator.truediv}
​
def postfix(stack):
  if isinstance(stack, str):
    stack = deque([int(x) if x.isdigit() else x for x in stack.split()])
  op = stack.pop()
  if isinstance(op, int) or isinstance(op, float):
    return op
  else:
    arg2 = postfix(stack)
    arg1 = postfix(stack)
    return op_map[op](arg1, arg2)
