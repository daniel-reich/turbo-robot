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
    ops = {'+', '-', '*', '//'}
    stack = []
    exp = exp.replace('/', '//').split()
    for i in exp:
        if i in ops:
            stack.append(i)
        else:
            if not stack[-1] in ops:
                stack.append(str(eval('{}{}{}'.format(stack.pop(), stack.pop(), i))))
            else:
                stack.append(i)
    if len(stack) == 1:
        return int(stack[0])
    return int(str(eval('{}{}{}'.format(stack[1], stack[0], stack[2]))))

