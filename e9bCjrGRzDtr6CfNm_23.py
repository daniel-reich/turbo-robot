"""


Consider the equation `ax-b=bx-3a+4` where `a` and `b` are constants. Create a
function that takes numbers `a` and `b` as arguments, and returns the solution
of the equation.

  * If the equation does not have a solution, return `"No solution"`.
  * If any number satisfies the equation, return `"Any number"`.

### Examples

    solve(1, 2) ➞ -3.0
    
    solve(-4, -6) ➞ 5.0
    
    solve(4, 1) ➞ -2.333

### Notes

Round your answer to three decimal places.

"""

def solve(a, b):
​
  try:
    return round(eval('((-3*a) + (4+b))/(a-b)'),3)
  except ZeroDivisionError:
    x = 93
    if eval('(a*x)-b == (b*x)-(3*a)+4') == True:
      return 'Any number'
    else:
      return 'No solution'

