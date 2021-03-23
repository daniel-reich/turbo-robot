"""


Create a function that takes a first-degree equation as a string and solves
it. If there would be more than one solution, the function must return
`"Infinite solutions"`.

### Examples

    solver("2*x + 1 = x") ➞ -1.0
    
    solver("7*x + x - 4 = 0") ➞ 0.5
    
    solver("x = x") ➞ "Infinite solutions"

### Notes

The given variable is always "x".

"""

def solver(eq):
  c = eval(eq.replace('=', '-(') + ')', {"x": 1j})
  try:  
    return -c.real / c.imag
  except ZeroDivisionError:
    return "Infinite solutions"

