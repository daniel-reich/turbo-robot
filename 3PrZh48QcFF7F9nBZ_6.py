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

import re
def solver(eq):
  i = eq.find("=")
  eq = re.sub(r'\s(?=x)','1',eq)
  def replacement(match):
    a,b,c = match.group(1,2,3)
    return str(float(a) * float(c)) if a.isdigit() and c.isdigit() else a + c
  eq = re.sub(r'([0-9x])(\*)([0-9x])',replacement,eq)
  print(eq)
  def x_values(string):
    return list(map(lambda x: float(x),re.findall(r'-?\d+(?=x)',string)))
  def constants(string):
    return list(map(lambda x: float(x),re.findall(r'-?\d+(?!x)',string)))
  x = sum(x_values(eq[:i])) - sum(x_values(eq[i::]))
  c = sum(constants(eq[i::])) - sum(constants(eq[:i]))
  print(x)
  print(c)
  return "Infinite solutions" if x == 0 or c == 0 else c / x

