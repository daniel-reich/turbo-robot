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

def calculator(n1, operator, n2):
  try: 
    return eval(str(n1)+operator+str(n2))
  except ZeroDivisionError:
    return "Can't divide by 0!"

