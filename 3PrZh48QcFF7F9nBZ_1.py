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
  
  eq = eq.replace('=', '==')
  solutions = []
  
  for x in range(-100, 101):
    if eval(eq) == True:
      solutions.append(x)
  
  if len(solutions) > 1:
    return 'Infinite solutions'
  elif len(solutions) == 1:
    return solutions[0]
  else:
    return 'Infinite solutions'

