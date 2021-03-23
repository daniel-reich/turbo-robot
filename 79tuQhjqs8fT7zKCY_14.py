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
    lst = []
    expr = expr.split(' ')
    for i in expr:
        if i.isdigit(): lst.append(i)
        else:
            a,b = lst.pop(),lst.pop()
            lst.append(str(eval(b+i+a)))
    return int(float(lst[0]))

