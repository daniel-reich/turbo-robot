"""


Create a function that takes a string and returns the right answer.

### Examples

    post_fix("2 2 +") ➞ 4
    
    post_fix("2 2 /") ➞ 1
    
    post_fix("8 4 / 9 * 3 1 * /") ➞ 54

### Notes

  * The operators `+ - * /` may be supported.
  * Output always returns an integer.

"""

def post_fix(expression):
    '''
    Returns the evaluation of expression, which is (sort of!) in post fix notation
    '''
    expression = expression.split()
    operands = [item for item in expression if item.isnumeric()]
    operators = [item for item in expression if item in '+-*/']
    expr = ''.join([operands[i]+op for i, op in enumerate(operators)]+[operands[-1]]) 
    
    return eval(expr)

