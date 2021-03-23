"""


Create a function that takes a mathematical expression as a string, list of
numbers on which the mathematical expression is to be calculated and return
the result as a list of string.

### Examples

    mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]
    
    mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]
    
    mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]

### Notes

  * List of numbers are positive integers.
  * In the algebraic expression x = `*`

"""

def mathematical(exp, numbers):
  answers = []
  for num in numbers:
    expression = exp.replace('y', str(num))
    equation, call = expression.split('=')[1], expression.split('=')[0]
    
    if 'x' in equation:
      equation = equation.replace('x', '*')
      
    if '^' in equation:
      equation = equation.replace('^', '**')
      
    answers.append('{0}={1:.0f}'.format(call, eval(equation)))
    
  else:
    return answers

