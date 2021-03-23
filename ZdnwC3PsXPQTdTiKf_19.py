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

def calculator(x,y,z):
  if z==0:
    return("Can't divide by 0!")
  else:
    if y=='+':
      return x+z
    elif y=='-':
      return x-z
    elif y=='*':
      return x*z
    else:
      return x/z

