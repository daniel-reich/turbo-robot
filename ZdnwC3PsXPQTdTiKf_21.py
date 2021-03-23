"""


Create a function that takes two numbers and a mathematical operator `+ - / *`
and will perform a calculation with the given numbers.

### Examples

    calculator(2, "+", 2) ➞ 4
    
    calculator(2, "*", 2) ➞ 4
    
    calculator(4, "/", 2) ➞ 2

### Notes

If the input tries to divide by 0, return: `"Can't divide by 0!"`

"""

import operator
def calculator(num1, op, num2):
  ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul} 
  if op == '/' and num2==0:
    return 'Can\'t divide by 0!'
  return ops[op](num1,num2)

