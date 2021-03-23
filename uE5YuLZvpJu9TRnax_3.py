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

def prefix(expr):
    '''
    Returns the result of evaluating expr, a valid arithmetic expression
    using prefix notation for operators.
    '''
    stack = []
    operators = ['/','*','+','-']
​
    for token in expr.split()[::-1]:
        if token not in operators:
            stack.append(int(token))
        else:
            if token == '/':
                token = '//'
            stack.append(eval('{} {} {}'.format(stack.pop(),token,stack.pop())))
​
    return stack[0]

