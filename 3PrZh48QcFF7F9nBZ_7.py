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
  eq = eq.replace('=', '-')
  i, p = 0, None
  while True:
    for m in [-1,1]:
      x = i * m
      v = eval(eq)
      if v == 0: return x
      if i > 0 and v == p: return "Infinite solutions"
      p = v
    i += 1

