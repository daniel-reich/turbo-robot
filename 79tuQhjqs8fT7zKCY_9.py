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

def postfix(expr):
  items = expr.split(" ")
  i = len(items)-1
​
  def recurse():
    nonlocal i
    op = items[i]
    i -= 1
    if "0" <= op <= "9":
      return int(op)
    if op == "+":
      return recurse()+recurse()
    if op == "-":  # next read item is second operand
      return -recurse()+recurse()
    if op == "*":
      return recurse()*recurse()
    if op == "/":  # ^
      return 1/recurse()*recurse()
    raise Exception("unsupported action: "+op)
​
  return recurse()

