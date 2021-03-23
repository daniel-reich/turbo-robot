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
  A=eq.split('=')
  leftc=eval(A[0].replace('x', '0'))
  rightc=eval(A[1].replace('x', '0'))
  eq2=eq.replace('x', '1x').replace(' ','').replace('*1x*1x','')
  B=eq2.split('=')
  p=r'[\d*?]+(?=x)'
  leftx=sum(eval(t.group()) for t in re.finditer(p,B[0]))
  rightx=sum(eval(t.group()) for t in re.finditer(p,B[1]))
  xc=leftx-rightx
  c=rightc-leftc
  if xc:
    return c/xc
  else:
    return "Infinite solutions"

