"""


Postfix notation is a mathematical notation in which operators follow their
operands. In other words, `pfexp1 pfexp2 op`, where `pfexp1` and `pfexp2` are
both postfix expressions.

Some examples:

  * `2 2 +` is the postfix notation of the expression `2 + 2`.
  * `2 3 * 1 - 5 /` is the postfix notation of the expression `((2 * 3) - 1) / 5`.

Here you have to compute the result from a postfix expression.

### Examples

    postfix("2 2 +") ➞ 4
    # 2 + 2 = 4
    
    postfix("2 3 * 1 - 5 /") ➞ 1
    # ((2 * 3) - 1) / 5 = (6 - 1) / 5 = 5 / 5 = 1

### Note

  * Operators and operands are separated by a space.
  * The operators `+, -, *, /` may be supported.
  * You can use Python list as a stack data structure to solve this problem.

"""

def get_result(operator, stack, top):
  if operator == "+":
    return stack[top-1] + stack[top], 2
  elif operator == "-":
    return stack[top-1] - stack[top], 2
  elif operator == "*":
    return stack[top-1] * stack[top], 2
  elif operator == "/":
    return stack[top-2] / stack[top], 2
  else:
    return stack[top]
​
class stack():
  def __init__(self):
    self.data = []
    self.top = -1
​
  def push(self, item):
    self.top += 1
    if self.top < len(self.data):
      self.data[self.top] = item
    else:
      self.data.append(item)
      
  def pop(self):
    if self.top > -1:
      ret = self.data[self.top]
      self.top -= 1
      return ret
​
def push_result(operator, working):
  op2 = working.pop()
  op1 = working.pop()
  if operator == "+":
    working.push(op1 + op2)
  elif operator == "-":
    working.push(op1 - op2)
  elif operator == "*":
    working.push(op1 * op2)
  elif operator == "/":
    working.push(op1 / op2)
  
def postfix(expr):
  lexpr = expr.split()
  working = stack()
  
  for item in lexpr:
    if item in {"+", "-", "*", "/"}:
      push_result(item, working)
    else:
      working.push(int(item))
  return working.pop()

